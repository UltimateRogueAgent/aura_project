from typing import Any, Dict
from .orchestrator import Orchestrator
from ..gui.theme_manager import ThemeManager
from .security import SecurityManager
from ..memory import VectorStoreManager, MemoryManager

class AuraApplication:
    """
    Main application class for AURA. It handles the initialization and
    lifecycle of the application, as well as the coordination between
    different components.
    """

    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.initialize()

    def initialize(self) -> None:
        """Initializes all components of the application."""
        print("Initializing AuraApplication...")

        # Security
        self.security_manager = SecurityManager(self.config.get("security", {}))

        # Memory
        vector_store_config = self.config.get("memory", {}).get("vector_store", {})
        self.vector_store = VectorStoreManager(config=vector_store_config)
        self.memory_manager = MemoryManager(self.vector_store, self.config.get("memory", {}))

        # Orchestrator
        self.orchestrator = Orchestrator(self.config)

        # GUI Managers
        self.theme_manager = ThemeManager()

    def start(self) -> None:
        """Starts the main application loop."""
        # This will be managed by main.py, which handles the QApplication loop.
        print("AuraApplication started.")
        pass

    def shutdown(self) -> None:
        """Shuts down the application gracefully."""
        print("Shutting down AuraApplication...")
        # Add any cleanup logic here
        pass

    def process_user_request(self, request: str) -> str:
        """
        Processes a user request by passing it to the orchestrator.
        """
        # Basic input validation/sanitization
        if not self.security_manager.validate_command(request):
            return "Request blocked due to security policy."

        print(f"Processing user request: '{request}'")
        return self.orchestrator.run_crew(request)

    def get_status(self) -> Dict[str, Any]:
        """Returns the current status of the application."""
        return {
            "status": "running",
            "memory_stats": self.memory_manager.get_statistics()
        }
