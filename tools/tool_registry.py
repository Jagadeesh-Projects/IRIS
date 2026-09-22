from tools.system_tools import get_system_info

from tools.file_tools import (
    search_files,
    list_directory
)

from tools.application_tools import (
    open_application
)


TOOLS = {

    "get_system_info":
        get_system_info,

    "search_files":
        search_files,

    "list_directory":
        list_directory,

    "open_application":
        open_application

}


def get_tool(tool_name):

    return TOOLS.get(tool_name)