# Copyright Exafunction, Inc.

# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
import asyncio
import gzip
import importlib.metadata
import locale
import logging
import os
import platform
import stat
import subprocess
import tempfile
import time
from urllib.request import urlretrieve

import aiohttp
import crc32c
import notebook

__version__ = importlib.metadata.version("codeium-jupyter")

API_SERVER_HOST = "server.codeium.com"
API_SERVER_PORT = 443
LANGUAGE_SERVER_MIN_PORT = 42200
LANGUAGE_SERVER_MAX_PORT = 42300
MANAGER_DIR_PORT_TIMEOUT_SEC = 10
CODEIUM_DEV_MODE_ENV_VAR = "CODEIUM_DEV_MODE"
HEARTBEAT_INTERVAL_SEC = 5

LANGUAGE_SERVER_VERSION = "1.1.11"
LANGUAGE_SERVER_CRC32C = {
    "language_server_linux_x64": "c0e33755",
    "language_server_linux_arm": "178b6861",
    "language_server_macos_x64": "b5a3b9e2",
    "language_server_macos_arm": "221ed591",
    "language_server_windows_x64.exe": "c541a37f",
}
LANGUAGE_SERVER_SHA = "c964787841154e81cc1042c44ee475d7b058722e"

arch_translations = {
    "arm64": "arm",
    "AMD64": "x64",
    "x86_64": "x64",
}


def get_language_server_name() -> str:
    """Get the name of the language server according to the os and architecture."""
    sysinfo = platform.uname()
    sys_architecture = sysinfo.machine

    if sys_architecture not in arch_translations:
        raise Exception(f"Unsupported platform: {sys_architecture}")

    arch = arch_translations[sys_architecture]

    if sysinfo.system == "Windows":
        if arch != "x64":
            raise Exception(f"Unsupported platform: Windows / {sys_architecture}")
        return "language_server_windows_x64.exe"
    if sysinfo.system == "Darwin":
        return f"language_server_macos_{arch}"
    if sysinfo.system == "Linux":
        return f"language_server_linux_{arch}"

    raise Exception(f"Unsupported platform: {sysinfo.system} / {sys_architecture}")


class Codeium:
    """Interface between the Jupyter Notebook and the Codeium language server."""

    def __init__(self):
        self.name = "codeium"
        self.install_dir = os.path.dirname(os.path.realpath(__file__))
        self.binary_dir = os.path.join(self.install_dir, "binaries")
        language_server_name = get_language_server_name()
        self.download_if_needed(language_server_name)
        self.start_language_server(language_server_name)
        asyncio.run_coroutine_threadsafe(self.heartbeat(), asyncio.get_event_loop())

    def download_if_needed(self, language_server_name: str):
        language_server_path = os.path.join(
            self.binary_dir, LANGUAGE_SERVER_SHA, language_server_name
        )
        if os.path.isfile(language_server_path):
            return
        self.download_language_server(language_server_name)

    def download_language_server(self, language_server_name: str):
        download_url = (
            f"https://github.com/Exafunction/codeium/releases/download/"
            f"language-server-v{LANGUAGE_SERVER_VERSION}/{language_server_name}.gz"
        )
        output_dir = os.path.join(self.binary_dir, LANGUAGE_SERVER_SHA)
        os.makedirs(output_dir, exist_ok=True)

        logging.info("Downloading language server from %s", download_url)
        zip_path, _ = urlretrieve(download_url)
        with open(zip_path, "rb") as f:
            crc = crc32c.crc32c(f.read())
            if crc != int(LANGUAGE_SERVER_CRC32C[language_server_name], 16):
                logging.error(
                    "CRC mismatch: %s vs %s",
                    hex(crc),
                    LANGUAGE_SERVER_CRC32C[language_server_name],
                )
                return
        with gzip.open(zip_path, "rb") as gzip_file:
            language_server_path = os.path.join(output_dir, language_server_name)
            with open(language_server_path, "wb") as language_server:
                language_server.write(gzip_file.read())

                # Make the file executable
                st = os.stat(language_server_path)
                new_mode = st.st_mode | stat.S_IEXEC
                if new_mode != st.st_mode:
                    os.chmod(language_server_path, new_mode)
        logging.info("Successfully downloaded language server to %s", output_dir)

    def start_language_server(self, language_server_name: str):
        language_server_path = os.path.join(
            self.binary_dir, LANGUAGE_SERVER_SHA, language_server_name
        )

        # Create manager directory
        manager_dir = os.path.join(tempfile.mkdtemp(), "codeium", "manager")
        os.makedirs(manager_dir, exist_ok=False)

        # Get port lock directory
        port_lock_dir = os.path.join(
            tempfile.gettempdir(), "codeium", "language_server_flocks"
        )
        os.makedirs(port_lock_dir, exist_ok=True)

        # Start language server
        logging.info("Starting language server")
        args = [
            language_server_path,
            "--api_server_host",
            API_SERVER_HOST,
            "--api_server_port",
            str(API_SERVER_PORT),
            "--min_port",
            str(LANGUAGE_SERVER_MIN_PORT),
            "--max_port",
            str(LANGUAGE_SERVER_MAX_PORT),
            "--manager_dir",
            manager_dir,
            "--port_lock_dir",
            port_lock_dir,
        ]
        # Check if we are in dev mode
        if os.environ.get(CODEIUM_DEV_MODE_ENV_VAR):
            args.append("--dev_mode")
        self._proc = subprocess.Popen(args)

        # Wait until a port file exists
        start_time = time.time()
        while True:
            files = os.listdir(manager_dir)
            files = [f for f in files if os.path.isfile(os.path.join(manager_dir, f))]
            if len(files) > 0:
                self.port = int(files[0])
                break

            if time.time() - start_time > 10:
                raise Exception("Language server port file not found after 10 seconds")
            time.sleep(0.1)

        logging.info("Language server started on port %d", self.port)
        self.base_url = (
            f"http://localhost:{self.port}/"
            f"exa.language_server_pb.LanguageServerService/"
        )

    async def heartbeat(self):
        """Send a heartbeat message to the language server."""
        while True:
            await self.make_language_server_request({"metadata": {}}, "heartbeat")
            await asyncio.sleep(HEARTBEAT_INTERVAL_SEC)

    async def make_language_server_request(self, data: dict, method: str) -> dict:
        if "metadata" in data:
            metadata = data["metadata"]
            metadata["ideName"] = "jupyter_notebook"
            metadata["ideVersion"] = notebook.__version__
            metadata["extensionVersion"] = __version__
            metadata["locale"] = locale.getdefaultlocale()[0]

        url = f"{self.base_url}{method}"
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=data) as resp:
                return await resp.json()

    async def request(self, data: dict) -> dict:
        method = data["method"]
        del data["method"]
        if method == "get_completions":
            return await self.make_language_server_request(data, "GetCompletions")
        if method == "accept_completion":
            return await self.make_language_server_request(data, "AcceptCompletion")
        if method == "heartbeat":
            return await self.make_language_server_request(data, "Heartbeat")
        if method == "record_event":
            return await self.make_language_server_request(data, "RecordEvent")
        if method == "cancel_request":
            return await self.make_language_server_request(data, "CancelRequest")
        raise Exception(f"Unknown method {method}")


if __name__ == "__main__":
    c = Codeium()
