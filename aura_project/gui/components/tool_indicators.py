from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QFrame
from PyQt6.QtCore import Qt

class ToolIndicator(QWidget):
    """
    A widget to visually indicate which tool is currently being used by an agent.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        """
        Initializes the user interface of the widget.
        """
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.frame = QFrame(self)
        self.frame_layout = QVBoxLayout(self.frame)

        self.label = QLabel("Active Tool: None")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.frame_layout.addWidget(self.label)
        self.layout.addWidget(self.frame)

        # This stylesheet can be expanded in the QSS files
        self.frame.setObjectName("toolIndicatorFrame")
        self.frame.setStyleSheet("""
            #toolIndicatorFrame {
                background-color: #2D3748;
                color: #E2E8F0;
                padding: 5px;
                border-radius: 5px;
                border: 1px solid #4A5568;
            }
        """)

    def set_active_tool(self, tool_name: str):
        """
        Updates the indicator to show the name of the currently active tool.

        Args:
            tool_name: The name of the tool to display.
        """
        if tool_name:
            self.label.setText(f"Active Tool: {tool_name}")
            self.show()
        else:
            self.label.setText("Active Tool: None")
            self.hide()
