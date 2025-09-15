from abc import ABC, abstractmethod
from typing import Any, Dict, List
from dataclasses import dataclass

@dataclass
class ToolResult:
    """
    Represents the result of a tool execution.
    """
    success: bool
    result: Any
    error_message: str = ""

class BaseTool(ABC):
    """
    Abstract base class for all tools.
    """

    def __init__(self, config: Dict[str, Any]):
        """
        Initializes the tool.

        Args:
            config: A dictionary containing configuration for the tool.
        """
        self.config = config

    @abstractmethod
    def execute(self, *args, **kwargs) -> ToolResult:
        """
        Executes the tool.
        """
        pass

    @abstractmethod
    def validate_input(self, *args, **kwargs) -> bool:
        """
        Validates the input for the tool.
        """
        pass

    @abstractmethod
    def get_description(self) -> str:
        """
        Gets the description of the tool.
        """
        pass

    @abstractmethod
    def get_schema(self) -> Dict[str, Any]:
        """
        Gets the schema of the tool's input and output.
        """
        pass

class ToolRegistry:
    """
    A registry for discovering and managing tools.
    """

    def __init__(self):
        self._tools: Dict[str, BaseTool] = {}

    def register_tool(self, name: str, tool: BaseTool):
        """
        Registers a tool.
        """
        self._tools[name] = tool

    def unregister_tool(self, name: str):
        """
        Unregisters a tool.
        """
        if name in self._tools:
            del self._tools[name]

    def get_tool(self, name: str) -> BaseTool:
        """
        Gets a tool by name.
        """
        return self._tools.get(name)

    def list_tools(self) -> List[str]:
        """
        Lists all registered tools.
        """
        return list(self._tools.keys())
