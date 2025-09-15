from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QMenuBar, QStatusBar
from PyQt6.QtGui import QAction, QKeySequence
from .chat_widget import ChatWidget
from .settings_panel import SettingsPanel
from ..core import AuraApplication

class MainWindow(QMainWindow):
    """
    The main window for the AURA application, serving as the primary
    container for all other GUI components.
    """

    def __init__(self, application: AuraApplication):
        super().__init__()
        self.application = application
        self.setWindowTitle("AURA - Autonomous Unit & Resource Arbitrator")
        # Set geometry as defined in design.md's default_config.yaml
        self.setGeometry(100, 100, 1400, 900)
        self.setMinimumSize(800, 600)

        # Central widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
        self.layout.setContentsMargins(0, 0, 0, 0) # Use full window space

        # Add the chat widget
        self.chat_widget = ChatWidget(self.application.orchestrator)
        self.layout.addWidget(self.chat_widget)

        self.settings_panel = SettingsPanel()

        self._create_menu_bar()
        self._create_status_bar()
        self._create_shortcuts()

    def show_settings_panel(self):
        """
        Shows the settings panel as a separate window.
        """
        if self.settings_panel.isVisible():
            self.settings_panel.activateWindow()
        else:
            self.settings_panel.show()

    def _create_menu_bar(self):
        """
        Creates and populates the menu bar for the main window.
        """
        self.menu_bar = self.menuBar()

        # File Menu
        file_menu = self.menu_bar.addMenu("&File")
        exit_action = QAction("E&xit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Edit Menu
        edit_menu = self.menu_bar.addMenu("&Edit")

        # View Menu
        view_menu = self.menu_bar.addMenu("&View")

        # Help Menu
        help_menu = self.menu_bar.addMenu("&Help")

    def _create_status_bar(self):
        """
        Creates the status bar for the main window.
        """
        self.status_bar = self.statusBar()
        self.status_bar.showMessage("Ready")

    def _create_shortcuts(self):
        """
        Creates keyboard shortcuts for common actions.
        """
        self.settings_shortcut = self.addAction(QAction("Preferences", self))
        self.settings_shortcut.setShortcut(QKeySequence("Ctrl+P"))
        self.settings_shortcut.triggered.connect(self.show_settings_panel)
