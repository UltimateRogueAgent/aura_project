from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QFrame
from PyQt6.QtCore import Qt

class AgentStatus(QWidget):
    """
    A card-like widget to display the name and current status of an agent.
    """

    def __init__(self, agent_name: str, parent=None):
        super().__init__(parent)
        self.agent_name = agent_name
        self.init_ui()

    def init_ui(self):
        """
        Initializes the user interface of the widget.
        """
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.frame = QFrame(self)
        self.frame.setObjectName("agentStatusFrame")
        self.frame_layout = QVBoxLayout(self.frame)

        self.name_label = QLabel(f"<b>{self.agent_name}</b>")
        self.name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.status_label = QLabel("Idle")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.status_label.setObjectName("statusLabel")

        self.frame_layout.addWidget(self.name_label)
        self.frame_layout.addWidget(self.status_label)
        self.layout.addWidget(self.frame)

        # Default styling, can be overridden by theme QSS
        self.frame.setStyleSheet("""
            #agentStatusFrame {
                background-color: @primary_color;
                color: @text_color;
                padding: 10px;
                border-radius: 5px;
                border: 1px solid @secondary_color;
                min-width: 150px;
            }
            #statusLabel {
                font-style: italic;
            }
        """)

    def set_status(self, status: str):
        """
        Updates the displayed status of the agent.

        Args:
            status: The new status message to display.
        """
        self.status_label.setText(status)
