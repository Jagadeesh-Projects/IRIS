import os
import shutil
import subprocess

from utils.logger import logger


APPLICATIONS = {

    "chrome": [
        "chrome.exe",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    ],

    "edge": [
        "msedge.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"
    ],

    "notepad": [
        "notepad.exe"
    ],

    "calculator": [
        "calc.exe"
    ],

    "paint": [
        "mspaint.exe"
    ],

    "vscode": [
        "code.exe",
        r"C:\Users\Public\Desktop\Visual Studio Code.lnk"
    ]
}


def _find_executable(candidates):
    """
    Find the first executable that exists
    or is available on PATH.
    """

    for candidate in candidates:

        # Check PATH
        path = shutil.which(candidate)

        if path:
            return path

        # Check exact filesystem path
        if os.path.exists(candidate):
            return candidate

    return None


def open_application(application_name):
    """
    Open a whitelisted Windows application.
    """

    application_name = (
        application_name
        .strip()
        .lower()
    )

    if application_name not in APPLICATIONS:

        return {
            "success": False,
            "error": (
                f"Application '{application_name}' "
                f"is not in the allowed application list."
            )
        }

    executable = _find_executable(
        APPLICATIONS[application_name]
    )

    if executable is None:

        return {
            "success": False,
            "error": (
                f"Could not find {application_name} "
                f"on this computer."
            )
        }

    try:

        subprocess.Popen(
            [executable]
        )

        logger.info(
            f"Opened application: {application_name}"
        )

        return {
            "success": True,
            "data": {
                "action": "OPEN",
                "application": application_name,
                "executable": executable
            }
        }

    except Exception as e:

        logger.error(
            f"Application launch error: {e}"
        )

        return {
            "success": False,
            "error": str(e)
        }