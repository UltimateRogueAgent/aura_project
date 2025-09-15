from PyQt6.QtWidgets import QWidget, QCheckBox, QSlider, QPushButton, QColorDialog, QFontDialog, QVBoxLayout, QHBoxLayout, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QFont

class ModernSwitch(QCheckBox):
    """
    A custom toggle switch with a modern look and feel.
    Styling is primarily handled via QSS for easy customization.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setObjectName("modernSwitch")
        # Basic styling can be defined here and overridden in theme QSS files
        self.setStyleSheet("""
            #modernSwitch::indicator {
                width: 40px;
                height: 20px;
            }
            #modernSwitch::indicator:unchecked {
                image: url(./assets/icons/toggle_off.png); /* Placeholder path */
            }
            #modernSwitch::indicator:checked {
                image: url(./assets/icons/toggle_on.png); /* Placeholder path */
            }
        """)

class ModernSlider(QSlider):
    """
    A custom slider with a modern aesthetic.
    Styling is handled via QSS.
    """
    def __init__(self, orientation, parent=None):
        super().__init__(orientation, parent)
        self.setObjectName("modernSlider")

class ColorPicker(QWidget):
    """
    A widget that allows the user to pick a color using QColorDialog.
    It displays the currently selected color.
    """
    colorChanged = Qt.pyqtSignal(QColor)

    def __init__(self, initial_color: QColor = QColor("white"), parent=None):
        super().__init__(parent)
        self._color = initial_color
        self.init_ui()

    def init_ui(self):
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.color_label = QLabel()
        self.color_label.setFixedSize(20, 20)
        self.update_color_label()

        self.button = QPushButton("Choose Color")
        self.button.clicked.connect(self.on_choose_color)

        self.layout.addWidget(self.color_label)
        self.layout.addWidget(self.button)

    def on_choose_color(self):
        color = QColorDialog.getColor(self._color, self, "Choose a color")
        if color.isValid():
            self._color = color
            self.update_color_label()
            self.colorChanged.emit(self._color)

    def update_color_label(self):
        self.color_label.setStyleSheet(f"background-color: {self._color.name()}; border: 1px solid #888; border-radius: 10px;")

    def color(self) -> QColor:
        return self._color

class FontSelector(QWidget):
    """
    A widget for selecting a font using QFontDialog.
    Displays the name of the currently selected font.
    """
    fontChanged = Qt.pyqtSignal(QFont)

    def __init__(self, initial_font: QFont = QFont("Segoe UI"), parent=None):
        super().__init__(parent)
        self._font = initial_font
        self.init_ui()

    def init_ui(self):
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.font_label = QLabel(self._font.family())
        self.font_label.setFont(self._font)

        self.button = QPushButton("Choose Font")
        self.button.clicked.connect(self.on_choose_font)

        self.layout.addWidget(self.font_label)
        self.layout.addWidget(self.button)

    def on_choose_font(self):
        font, ok = QFontDialog.getFont(self._font, self, "Choose a font")
        if ok:
            self._font = font
            self.font_label.setText(self._font.family())
            self.font_label.setFont(self._font)
            self.fontChanged.emit(self._font)

    def font(self) -> QFont:
        return self._font
