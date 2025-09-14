# Project Structure

## Directory Organization

```text
aura_project/
├── config/                  # Central configuration management
│   ├── __init__.py
│   ├── settings.py          # ConfigManager class - YAML configuration loader
│   ├── default_config.yaml  # Default application settings
│   └── themes/              # GUI theme definitions
│       ├── dark.yaml
│       ├light.yaml
│       └── custom.yaml
├── core/                    # Core application logic
│   ├── __init__.py
│   ├── application.py       # AuraApplication - main app coordinator
│   └── event_manager.py     # Inter-component communication
├── agents/                  # CrewAI agent implementations
│   ├── __init__.py
│   ├── base_agent.py        # BaseAgent abstract class
│   ├── researcher.py        # ResearcherAgent - web research & data gathering
│   ├── coder.py            # CoderAgent - file operations & code management
│   └── designer.py         # DesignerAgent - solution planning & architecture
├── tools/                   # Agent tool implementations
│   ├── __init__.py
│   ├── base_tool.py        # BaseTool interface
│   ├── file_tools.py       # File system operations (read/write/list)
│   ├── web_tools.py        # Playwright scraping & DuckDuckGo search
│   └── mcp_tools.py        # Model Context Protocol integration
├── memory/                  # Long-term memory system
│   ├── __init__.py
│   ├── vector_store.py     # ChromaDB integration & VectorStoreManager
│   └── memory_manager.py   # Context management & memory optimization
├── gui/                     # PyQt6 user interface
│   ├── __init__.py
│   ├── main_window.py      # MainWindow - primary application window
│   ├── chat_widget.py      # ChatWidget - real-time chat interface
│   ├── settings_panel.py   # Advanced configuration interface
│   ├── theme_manager.py    # Theme switching & color management
│   ├── animation_manager.py # UI animations & transitions
│   ├── components/         # Reusable UI components
│   │   ├── __init__.py
│   │   ├── progress_widgets.py
│   │   ├── agent_status.py
│   │   ├── tool_indicators.py
│   │   ├── notification_system.py
│   │   └── modern_controls.py
│   └── styles/             # QSS stylesheets
│       ├── dark_theme.qss
│       ├── light_theme.qss
│       └── animations.qss
├── integrations/           # External service clients
│   ├── __init__.py
│   ├── ollama_client.py    # OllamaClient - LLM communication
│   └── mcp_client.py       # MCPClient - protocol server discovery
├── utils/                  # Shared utilities
│   ├── __init__.py
│   ├── logging.py          # Centralized logging system
│   └── validators.py       # Input validation & security checks
├── assets/                 # Static resources
│   ├── icons/              # Application icons
│   ├── fonts/              # Custom fonts
│   └── animations/         # Animation assets
├── tests/                  # Test suite
│   ├── unit/               # Unit tests for individual components
│   ├── integration/        # Integration tests for workflows
│   ├── security/           # Security validation tests
│   └── fixtures/           # Test data and mocks
├── main.py                 # Application entry point
└── requirements.txt        # Python dependencies
```

## Key Architectural Principles

### Modular Design

- Each directory represents a distinct functional area
- Clear interfaces between modules via `__init__.py` exports
- Minimal coupling between components

### Configuration-Driven

- All settings centralized in `config/default_config.yaml`
- Runtime configuration changes supported
- Environment-specific overrides via `.env` files

### Security Boundaries

- File operations restricted to safe directories
- Command execution validation in `utils/validators.py`
- MCP tool security checks before execution

### Agent-Tool Separation

- Agents in `/agents/` define behavior and coordination
- Tools in `/tools/` provide atomic capabilities
- Clean interface allows easy tool addition/removal

## Import Conventions

### Module Imports

```python
# Core components
from core.application import AuraApplication
from config.settings import ConfigManager

# Agents
from agents.researcher import ResearcherAgent
from agents.coder import CoderAgent
from agents.designer import DesignerAgent

# Tools
from tools.web_tools import WebTools
from tools.file_tools import FileTools
from tools.mcp_tools import MCPTools

# GUI
from gui.main_window import MainWindow
from gui.chat_widget import ChatWidget
```

### Configuration Access

```python
# Always access config through ConfigManager
config = ConfigManager()
ollama_host = config.get('ollama.host', 'localhost')
theme_name = config.get('gui.theme.name', 'dark')
```

## File Naming Conventions

- **Classes**: PascalCase (e.g., `ResearcherAgent`, `ConfigManager`)
- **Files**: snake_case (e.g., `main_window.py`, `vector_store.py`)
- **Constants**: UPPER_SNAKE_CASE (e.g., `DEFAULT_TIMEOUT`, `MAX_CONTEXT_LENGTH`)
- **Configuration**: kebab-case for YAML keys (e.g., `ollama-host`, `max-search-results`)

## Testing Structure

- **Unit tests**: Mirror source structure in `tests/unit/`
- **Integration tests**: Workflow testing in `tests/integration/`
- **Security tests**: Validation testing in `tests/security/`
- **Fixtures**: Shared test data in `tests/fixtures/`

## Development Workflow

1. **Configuration**: Start with `config/default_config.yaml` for new features
2. **Core Logic**: Implement business logic in appropriate module
3. **Tools**: Add capabilities in `/tools/` with security validation
4. **Agents**: Wire tools to agents in `/agents/`
5. **GUI**: Create interface components in `/gui/`
6. **Integration**: Connect components via `core/application.py`
7. **Testing**: Add comprehensive tests following structure

## Communication Guidelines

- **User Responses**: Always respond to users in Polish language
- **Code Comments**: Use English for code documentation and technical terms
- **Error Messages**: Polish for user-facing messages, English for technical logs
- **GUI Labels**: Polish for all user interface elements
