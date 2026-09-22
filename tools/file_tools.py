import os

from utils.logger import logger


EXCLUDED_DIRECTORIES = {
    ".venv",
    "__pycache__",
    ".git",
    ".idea",
    ".vscode"
}


def search_files(
    directory,
    keyword="",
    extension=None,
    max_results=50
):
    """
    Search recursively for files.
    """

    results = []

    try:

        if not os.path.isdir(directory):

            return {
                "success": False,
                "error": f"Directory does not exist: {directory}"
            }

        if extension:

            extension = extension.lower()

        for root, directories, files in os.walk(directory):

            directories[:] = [
                directory_name
                for directory_name in directories
                if directory_name not in EXCLUDED_DIRECTORIES
            ]

            for filename in files:

                filename_lower = filename.lower()

                if keyword:

                    if keyword.lower() not in filename_lower:
                        continue

                if extension:

                    if not filename_lower.endswith(extension):
                        continue

                full_path = os.path.join(
                    root,
                    filename
                )

                results.append(full_path)

                if len(results) >= max_results:
                    break

            if len(results) >= max_results:
                break

        logger.info(
            f"File search completed: {len(results)} results"
        )

        return {
            "success": True,
            "count": len(results),
            "files": results,
            "max_results": max_results
        }

    except Exception as e:

        logger.error(
            f"File search error: {e}"
        )

        return {
            "success": False,
            "error": str(e)
        }


def list_directory(
    directory,
    max_results=50
):
    """
    List files and folders in a directory.
    """

    results = []

    try:

        if not os.path.isdir(directory):

            return {
                "success": False,
                "error": f"Directory does not exist: {directory}"
            }

        for item in os.listdir(directory):

            if item in EXCLUDED_DIRECTORIES:
                continue

            full_path = os.path.join(
                directory,
                item
            )

            item_type = (
                "folder"
                if os.path.isdir(full_path)
                else "file"
            )

            results.append({
                "name": item,
                "type": item_type,
                "path": full_path
            })

            if len(results) >= max_results:
                break

        logger.info(
            f"Directory listing completed: {len(results)} results"
        )

        return {
            "success": True,
            "count": len(results),
            "items": results
        }

    except Exception as e:

        logger.error(
            f"Directory listing error: {e}"
        )

        return {
            "success": False,
            "error": str(e)
        }