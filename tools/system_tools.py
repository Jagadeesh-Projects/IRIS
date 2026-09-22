import platform
import psutil

from utils.logger import logger


def get_system_info():
    """
    Collect basic read-only information
    about the user's computer.
    """

    try:

        cpu_usage = psutil.cpu_percent(
            interval=1
        )

        memory = psutil.virtual_memory()

        disk = psutil.disk_usage("/")

        system_info = {
            "operating_system": platform.system(),
            "os_version": platform.version(),
            "processor": platform.processor(),
            "cpu_usage_percent": cpu_usage,
            "ram_total_gb": round(
                memory.total / (1024 ** 3),
                2
            ),
            "ram_used_gb": round(
                memory.used / (1024 ** 3),
                2
            ),
            "ram_usage_percent": memory.percent,
            "disk_total_gb": round(
                disk.total / (1024 ** 3),
                2
            ),
            "disk_free_gb": round(
                disk.free / (1024 ** 3),
                2
            )
        }

        logger.info(
            "System information collected"
        )

        return system_info

    except Exception as e:

        logger.error(
            f"System information error: {e}"
        )

        return {
            "error": str(e)
        }