from typing import Dict, Any, List
from ..utils.validators import is_safe_path, is_safe_command
from PyQt6.QtWidgets import QMessageBox

class SecurityManager:
    """
    Manages security-related aspects of the application, including
    path and command validation, user confirmations, and audit logging.
    """

    def __init__(self, config: Dict[str, Any]):
        """
        Initializes the SecurityManager with a given configuration.

        Args:
            config: A dictionary containing security settings, such as
                    allowed paths and blocked commands.
        """
        self.config = config
        self.allowed_paths = self.config.get("allowed_paths", [])
        self.blocked_commands = self.config.get("blocked_commands", [])
        self.sandbox_mode = self.config.get("sandbox_mode", True)

    def validate_path(self, path: str, check_sandbox: bool = True) -> bool:
        """
        Validates a file path. If check_sandbox is True, it enforces the sandbox rules.
        """
        if check_sandbox and self.sandbox_mode:
            return is_safe_path(path, self.allowed_paths)
        return True if not check_sandbox else is_safe_path(path, self.allowed_paths)

    def validate_command(self, command: str) -> bool:
        """
        Validates a command against the list of blocked commands.
        """
        if self.sandbox_mode:
            return is_safe_command(command, self.blocked_commands)
        return is_safe_command(command, self.blocked_commands)

    def validate_mcp_tool(self, tool_name: str) -> bool:
        """
        Validates an MCP tool. Placeholder for future implementation.
        """
        print(f"Validating MCP tool: {tool_name}")
        return True

    def request_confirmation(self, message: str, title: str = "Security Confirmation") -> bool:
        """
        Displays a confirmation dialog to the user for potentially
        dangerous operations.
        """
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Warning)
        msg_box.setText(message)
        msg_box.setWindowTitle(title)
        msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        msg_box.setDefaultButton(QMessageBox.StandardButton.No)

        return msg_box.exec() == QMessageBox.StandardButton.Yes

    def log_security_event(self, event: str):
        """
        Logs a security-related event. In a real application, this would
        write to a dedicated, secure log file.
        """
        print(f"[SECURITY EVENT] {event}")
