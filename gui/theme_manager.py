import yaml
import os
from typing import Dict, Any
from PyQt6.QtWidgets import QWidget, QApplication

class ThemeManager:
    """
    Manages the application's visual theme, including colors and styles
    loaded from YAML configuration files.
    """

    def __init__(self, theme_dir: str = "aura_project/config/themes", style_dir: str = "aura_project/gui/styles"):
        self.theme_dir = theme_dir
        self.style_dir = style_dir
        self.themes: Dict[str, Any] = {}
        self.current_theme_name: str = ""
        self.current_palette: Dict[str, str] = {}
        self._load_themes()

    def _load_themes(self):
        """
        Loads all theme configurations from the specified theme directory.
        """
        if not os.path.isdir(self.theme_dir):
            print(f"Warning: Theme directory not found at '{self.theme_dir}'")
            return

        for filename in os.listdir(self.theme_dir):
            if filename.endswith(".yaml"):
                theme_name = os.path.splitext(filename)[0]
                filepath = os.path.join(self.theme_dir, filename)
                with open(filepath, 'r') as f:
                    self.themes[theme_name] = yaml.safe_load(f)

    def load_theme(self, theme_name: str) -> None:
        """
        Loads and applies a theme to the entire application.
        This includes setting the color palette and applying the QSS stylesheet.
        """
        if theme_name not in self.themes:
            raise ValueError(f"Theme '{theme_name}' not found.")

        self.current_theme_name = theme_name
        self.current_palette = self.themes[theme_name]

        qss_path = os.path.join(self.style_dir, f"{theme_name}_theme.qss")
        if os.path.exists(qss_path):
            with open(qss_path, "r") as f:
                style_sheet = f.read()
                # Here we can replace placeholders in QSS with palette colors
                for color_name, color_value in self.current_palette.items():
                    style_sheet = style_sheet.replace(f"@{color_name}", color_value)

                if QApplication.instance():
                    QApplication.instance().setStyleSheet(style_sheet)
        else:
            print(f"Warning: Stylesheet not found for theme '{theme_name}' at '{qss_path}'")

    def apply_animations(self, widget: QWidget) -> None:
        """
        A placeholder for applying theme-specific animations to a widget.
        """
        # This could be expanded to use QPropertyAnimation based on theme settings.
        print(f"Applying animations for theme '{self.current_theme_name}' to widget: {widget}")

    def get_color_palette(self) -> Dict[str, str]:
        """
        Returns the color palette of the currently loaded theme.
        """
        return self.current_palette

    def set_custom_colors(self, colors: Dict[str, str]) -> None:
        """
        Overrides colors in the current theme's palette and reapplies the theme.
        """
        if not self.current_theme_name:
            raise ValueError("No theme is currently loaded.")

        self.current_palette.update(colors)
        # Re-apply the theme with the updated colors
        self.load_theme(self.current_theme_name)
        print("Custom colors applied and theme reloaded.")
