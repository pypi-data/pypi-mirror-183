import os
import platform
import sys


def check_os():
    system = platform.system().lower()
    if system == "windows":
        return "windows"
    elif str(system).startswith("linux") or str(sys.platfrom).startswith("freebsd"):
        if "ANDROID_ARGUMENT" in os.environ:
            return "android"
        return "linux"
    elif system == "darwin":
        return "macosx"
