from PyQt6.QtWidgets import QProgressBar
from PyQt6.QtCore import Qt

class ModernProgressBar(QProgressBar):
    """
    A custom progress bar with a modern aesthetic, suitable for the AURA application.
    It can be styled further using the application's QSS stylesheets.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setRange(0, 100)
        self.setValue(0)
        self.setTextVisible(True)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setObjectName("modernProgressBar")

        # This provides a default style that can be overridden by the theme's QSS.
        self.setStyleSheet("""
            #modernProgressBar {
                border: 1px solid @secondary_color;
                border-radius: 5px;
                text-align: center;
                background-color: @primary_color;
                color: @text_color;
            }
            #modernProgressBar::chunk {
                background-color: @accent_color;
                width: 10px;
                margin: 1px;
            }
        """)
