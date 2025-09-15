from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import QTimer
from ...gui.animation_manager import AnimationManager

class NotificationSystem(QWidget):
    """
    A widget for displaying non-intrusive notifications with animations.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.animation_manager = AnimationManager()
        self.init_ui()
        self.hide()  # Start hidden

    def init_ui(self):
        """
        Initializes the user interface of the notification widget.
        """
        self.layout = QVBoxLayout(self)
        self.label = QLabel("")
        self.layout.addWidget(self.label)
        self.setObjectName("notificationWidget")

        # Default styling
        self.setStyleSheet("""
            #notificationWidget {
                background-color: @primary_color;
                color: @text_color;
                padding: 10px;
                border-radius: 5px;
            }
        """)

    def show_notification(self, message: str, level: str = "info", duration: int = 3000):
        """
        Displays a notification with a message and a specified level.

        Args:
            message: The message to display in the notification.
            level: The notification level ('info', 'success', 'warning', 'error').
            duration: The duration to display the notification in milliseconds.
        """
        self.label.setText(message)

        # Set style based on level
        if level == "info":
            self.setStyleSheet("background-color: @accent_color; color: white; padding: 10px; border-radius: 5px;")
        elif level == "success":
            self.setStyleSheet("background-color: @success_color; color: white; padding: 10px; border-radius: 5px;")
        elif level == "warning":
            self.setStyleSheet("background-color: @warning_color; color: black; padding: 10px; border-radius: 5px;")
        elif level == "error":
            self.setStyleSheet("background-color: @error_color; color: white; padding: 10px; border-radius: 5px;")

        self.show()
        # Position it at the top right of the parent
        if self.parentWidget():
            self.move(self.parentWidget().width() - self.width() - 10, 10)

        self.animation_manager.slide_in(self, direction="top")

        # Hide after a delay
        QTimer.singleShot(duration, self.hide)
