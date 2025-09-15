import psutil
from PyQt6.QtWidgets import QMessageBox

def check_system_requirements(min_ram_gb: int = 8):
    """
    Checks if the system meets the minimum RAM requirement and warns the user if not.
    """
    ram_gb = psutil.virtual_memory().total / (1024**3)
    if ram_gb < min_ram_gb:
        title = "System Requirements Warning"
        message = (
            f"AURA requires at least {min_ram_gb}GB of RAM to function optimally. "
            f"Your system has only {ram_gb:.2f}GB available.\n\n"
            "The application may run slowly or experience issues."
        )
        # This will show a warning dialog to the user.
        # Note: This requires a QApplication instance to be running.
        QMessageBox.warning(None, title, message)
        print(f"Warning: System RAM ({ram_gb:.2f}GB) is below the recommended {min_ram_gb}GB.")
    else:
        print(f"System RAM check passed: {ram_gb:.2f}GB available.")
