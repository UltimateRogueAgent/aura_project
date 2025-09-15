# AURA Configuration Management
from pathlib import Path
from typing import Any, Dict, Optional
import yaml


class ConfigManager:
    """Central configuration manager with YAML support and validation."""

    def __init__(self, config_path: Optional[Path] = None):
        self.config_path = config_path or Path(__file__).parent / "default_config.yaml"
        self._config: Dict[str, Any] = {}
        self._load_config()

    def _load_config(self) -> None:
        """Load configuration from YAML file."""
        try:
            if self.config_path.exists():
                with open(self.config_path, "r", encoding="utf-8") as f:
                    self._config = yaml.safe_load(f) or {}
            else:
                self._create_default_config()
        except Exception as e:
            print(f"Error loading config: {e}")
            self._config = {}

    def _create_default_config(self) -> None:
        """Create default configuration file."""
        default_config = {
            "application": {
                "name": "AURA",
                "version": "1.0.0",
                "debug": False,
                "log_level": "INFO",
            },
            "ollama": {
                "host": "localhost",
                "port": 11434,
                "orchestrator_model": "rogue-v1-brain",
                "agent_model": "rogue-v1-agent",
                "timeout": 30,
            },
            "memory": {
                "vector_store": {
                    "type": "chromadb",
                    "path": "./data/chroma_db",
                    "collection_name": "aura_memory",
                },
                "context_window": 8000,
                "max_memories": 10000,
            },
            "gui": {
                "theme": {
                    "name": "dark",
                    "primary_color": "#2D3748",
                    "accent_color": "#63B3ED",
                },
                "window": {"size": [1400, 900], "min_size": [800, 600]},
            },
        }

        self.config_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.config_path, "w", encoding="utf-8") as f:
            yaml.dump(default_config, f, default_flow_style=False, indent=2)
        self._config = default_config

    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value using dot notation."""
        keys = key.split(".")
        value = self._config

        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default

        return value

    def set(self, key: str, value: Any) -> None:
        """Set configuration value using dot notation."""
        keys = key.split(".")
        config = self._config

        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]

        config[keys[-1]] = value
        self._save_config()

    def get_section(self, section: str) -> Dict[str, Any]:
        """Get entire configuration section."""
        return self.get(section, {})

    def reload(self) -> None:
        """Reload configuration from file."""
        self._load_config()

    def validate(self) -> bool:
        """Validate configuration structure."""
        required_sections = ["application", "ollama", "memory", "gui"]
        return all(section in self._config for section in required_sections)

    def _save_config(self) -> None:
        """Save current configuration to file."""
        try:
            with open(self.config_path, "w", encoding="utf-8") as f:
                yaml.dump(self._config, f, default_flow_style=False, indent=2)
        except Exception as e:
            print(f"Error saving config: {e}")
