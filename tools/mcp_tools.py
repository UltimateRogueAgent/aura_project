from typing import Any, Dict
from ..integrations.mcp_client import MCPClient
from .base_tool import BaseTool, ToolResult

class MCPTools(BaseTool):
    """
    A tool for executing tools on remote MCP servers. It acts as a bridge
    between the agent's tool usage and the MCP client.
    """

    def __init__(self, config: Dict[str, Any], mcp_client: MCPClient):
        super().__init__(config)
        self.mcp_client = mcp_client

    def execute(self, server_name: str, tool_name: str, params: Dict) -> ToolResult:
        """
        Executes a remote tool on a specified MCP server.

        Args:
            server_name: The name of the MCP server to execute the tool on.
            tool_name: The name of the tool to execute.
            params: A dictionary of parameters for the tool.

        Returns:
            A ToolResult object with the outcome of the remote tool execution.
        """
        try:
            if not self.validate_input(server_name=server_name, tool_name=tool_name, params=params):
                 return ToolResult(success=False, result=None, error_message="Invalid input for MCP tool execution.")

            result = self.mcp_client.execute_tool(server_name, tool_name, params)
            return ToolResult(success=True, result=result)
        except ConnectionError as e:
            # Placeholder for a more sophisticated fallback mechanism.
            print(f"Connection error executing tool '{tool_name}' on server '{server_name}'. Fallback not implemented.")
            return ToolResult(success=False, result=None, error_message=str(e))
        except Exception as e:
            return ToolResult(success=False, result=None, error_message=f"An unexpected error occurred during MCP tool execution: {e}")

    def validate_input(self, **kwargs) -> bool:
        """
        Validates the input parameters for executing a remote tool.
        """
        return (
            "server_name" in kwargs and
            "tool_name" in kwargs and
            "params" in kwargs and
            isinstance(kwargs.get("server_name"), str) and
            isinstance(kwargs.get("tool_name"), str) and
            isinstance(kwargs.get("params"), dict)
        )

    def get_description(self) -> str:
        """
        Returns a description of what this tool does.
        """
        return "Executes a specified tool on a remote MCP server."

    def get_schema(self) -> Dict[str, Any]:
        """
        Returns the schema for the tool's input and output.
        """
        return {
            "name": "mcp_tool_executor",
            "description": self.get_description(),
            "args": {
                "server_name": "The name of the target MCP server.",
                "tool_name": "The name of the tool to be executed.",
                "params": "A dictionary of parameters for the tool."
            },
            "returns": "The result of the remote tool execution."
        }
