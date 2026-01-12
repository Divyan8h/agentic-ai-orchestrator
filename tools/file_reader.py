from langchain_community.agent_toolkits import FileManagementToolkit
from agent.schemas import FileSummary, ErrorResponse

file_toolkit = FileManagementToolkit(root_dir="sandbox")
read_file_tool = next(tool for tool in file_toolkit.get_tools() if tool.name == "read_file")

def read_file(path: str) -> FileSummary | ErrorResponse:
    try:
        content = read_file_tool.run(path)
        return FileSummary(
            title=path,
            summary=content[:300],
            key_points=content.split("\n")[:5]
        )
    except Exception as e:
        return ErrorResponse(error_type="FILE_READ_ERROR", message=str(e), recoverable=False)
