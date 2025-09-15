import os
from pathlib import Path
from typing import Any, Dict, List

from .base_tool import BaseTool, ToolResult


class FileTools(BaseTool):
    """
    A tool for performing file system operations within a sandboxed environment.
    """

    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        # Resolve the sandbox path to an absolute path for security checks.
        self.sandbox_path = Path(self.config.get("sandbox_path", "./workspace")).resolve()
        # Create the sandbox directory if it doesn't exist.
        if not self.sandbox_path.exists():
            self.sandbox_path.mkdir(parents=True, exist_ok=True)

    def _sanitize_path(self, path: str) -> Path:
        """
        Sanitizes a given path to prevent directory traversal attacks.
        Ensures that the resolved path is within the designated sandbox directory.

        Raises:
            PermissionError: If the path is outside the sandbox.
        """
        # This is a critical security measure.
        full_path = (self.sandbox_path / path).resolve()

        if self.sandbox_path not in full_path.parents and full_path != self.sandbox_path:
            raise PermissionError("Access to path outside of the sandbox is denied.")

        return full_path

    def execute(self, operation: str, **kwargs) -> ToolResult:
        """
        Executes a file system operation based on the provided operation name.

        Args:
            operation: The name of the operation to perform (e.g., 'read', 'write', 'list').
            **kwargs: The arguments for the specific operation.

        Returns:
            A ToolResult object indicating the outcome of the operation.
        """
        try:
            if not self.validate_input(operation, **kwargs):
                return ToolResult(success=False, result=None, error_message="Invalid input for the operation.")

            if operation == "read":
                return self._read_file(**kwargs)
            elif operation == "write":
                return self._write_file(**kwargs)
            elif operation == "list":
                return self._list_files(**kwargs)
            else:
                return ToolResult(success=False, result=None, error_message=f"Unsupported operation: {operation}")
        except PermissionError as e:
            return ToolResult(success=False, result=None, error_message=str(e))
        except Exception as e:
            return ToolResult(success=False, result=None, error_message=f"An unexpected error occurred: {e}")

    def _read_file(self, path: str) -> ToolResult:
        sanitized_path = self._sanitize_path(path)
        if not sanitized_path.is_file():
            return ToolResult(success=False, result=None, error_message=f"File not found: {path}")

        content = sanitized_path.read_text()
        return ToolResult(success=True, result=content)

    def _write_file(self, path: str, content: str) -> ToolResult:
        sanitized_path = self._sanitize_path(path)
        # Ensure parent directories exist before writing the file.
        sanitized_path.parent.mkdir(parents=True, exist_ok=True)
        sanitized_path.write_text(content)
        return ToolResult(success=True, result=f"File written to {path}")

    def _list_files(self, path: str = ".") -> ToolResult:
        sanitized_path = self._sanitize_path(path)
        if not sanitized_path.is_dir():
             return ToolResult(success=False, result=None, error_message=f"Directory not found: {path}")

        files = [f.name for f in sanitized_path.iterdir()]
        return ToolResult(success=True, result=files)

    def validate_input(self, operation: str, **kwargs) -> bool:
        if operation == "read":
            return "path" in kwargs and isinstance(kwargs["path"], str)
        elif operation == "write":
            return "path" in kwargs and "content" in kwargs and isinstance(kwargs["path"], str) and isinstance(kwargs["content"], str)
        elif operation == "list":
            # Path is optional for list.
            return True
        return False

    def get_description(self) -> str:
        return "A tool for file system operations: read, write, list. All paths are relative to a secure sandbox environment."

    def get_schema(self) -> Dict[str, Any]:
        return {
            "name": "file_tools",
            "description": self.get_description(),
            "operations": {
                "read": {
                    "description": "Reads the content of a specified file.",
                    "args": {"path": "str"},
                    "returns": "str"
                },
                "write": {
                    "description": "Writes content to a specified file.",
                    "args": {"path": "str", "content": "str"},
                    "returns": "str"
                },
                "list": {
                    "description": "Lists files in a specified directory.",
                    "args": {"path": "str (optional, defaults to sandbox root)"},
                    "returns": "List[str]"
                }
            }
        }
