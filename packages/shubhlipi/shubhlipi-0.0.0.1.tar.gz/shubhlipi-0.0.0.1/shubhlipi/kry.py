import sys
from pathlib import Path
from threading import Thread
from winregistry import WinRegistry
import base64

argv = sys.argv[1:]
tool = str(Path.home()) + "\\upakaraNAni\\bin"

REG = WinRegistry()

def from_base64(v: str) -> str:
    """Convert Text from ``base64`` to ``utf-8``"""
    return base64.b64decode(v).decode("utf-8")


def to_base64(v: str) -> str:
    """Convert Text from ``utf-8`` to ``base64``"""
    return base64.b64encode(bytes(v, "utf-8")).decode("utf-8")

def env(key: str) -> str:
    return from_base64(
        REG.read_entry("HKCU\\SOFTWARE\\" + to_base64("lipivars"), key).value
    )

def args(i: int) -> str:
    if i > len(argv) - 1:
        return ""
    else:
        return argv[i]


def get_type(val) -> str:
    return str(type(val))[8:-2]


def home() -> str:
    """Get ``home`` path for windows"""
    return str(Path.home())


def start_thread(f: str, daemon=False, join=False):
    th = Thread(target=f)
    th.daemon = daemon
    th.start()
    if join:
        th.join()
    return th
