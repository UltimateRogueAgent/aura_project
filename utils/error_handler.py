class ConfigError(Exception):
    """Custom exception for configuration errors."""
    pass

class ConnectionError(Exception):
    """Custom exception for connection errors."""
    pass

class AgentError(Exception):
    """Custom exception for agent execution errors."""
    pass

class SecurityError(Exception):
    """Custom exception for security errors."""
    pass


from PyQt6.QtWidgets import QMessageBox

class ErrorHandler:
    """A centralized error handler for the application."""

    def handle_configuration_error(self, error: ConfigError):
        """Handles configuration errors."""
        self.show_error_message("Configuration Error", str(error))

    def handle_connection_error(self, error: ConnectionError):
        """Handles connection errors."""
        self.show_error_message("Connection Error", str(error))

    def handle_agent_error(self, error: AgentError):
        """Handles agent errors."""
        self.show_error_message("Agent Error", str(error))

    def handle_security_error(self, error: SecurityError):
        """Handles security errors."""
        self.show_error_message("Security Error", str(error))

    def log_error(self, error: Exception, context: dict):
        """Logs an error with context."""
        print(f"An unexpected error occurred: {error} with context {context}")
        self.show_error_message("Unexpected Error", str(error))

    def show_error_message(self, title: str, message: str):
        """Displays an error message to the user."""
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Critical)
        msg_box.setText(message)
        msg_box.setWindowTitle(title)
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_box.exec()
