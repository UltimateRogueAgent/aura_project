# Technology Stack

## Core Framework & Architecture

- **GUI Framework**: PyQt6 for modern desktop interface with dark/light themes and animations
- **Agent Orchestration**: CrewAI with hierarchical process management
- **LLM Integration**: Ollama for local model hosting (rogue-v1-brain for orchestrator, rogue-v1-agent for specialized agents)
- **Vector Memory**: ChromaDB for long-term knowledge storage and retrieval
- **Configuration**: YAML-based central configuration with python-dotenv for environment variables

## Key Libraries

### AI & Language Models

- `crewai` - Multi-agent orchestration framework
- `crewai-tools` - Additional tools for CrewAI agents
- `langchain-community` - Community LangChain integrations
- `langchain-ollama` - Ollama integration for LangChain
- `ollama` - Direct Ollama client library

### Web & Data Processing

- `playwright` - Advanced web scraping and browser automation
- `beautifulsoup4` - HTML parsing and content cleaning
- `duckduckgo-search` - Privacy-focused search functionality

### Storage & Memory

- `chromadb` - Vector database for embeddings and memory

### GUI & Interface

- `pyqt6` - Modern desktop GUI framework

### Utilities

- `python-dotenv` - Environment variable management

## Development Environment Setup

### Prerequisites

1. **Python 3.9+** with virtual environment support
2. **Ollama** installed and running locally
3. **Git** for version control

### Installation Commands

```powershell
# Create and activate virtual environment
python -m venv aura_env
aura_env\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install
```

### Common Development Commands

```powershell
# Run the application
python main.py

# Run with debug mode
python main.py --debug

# Run tests
pytest tests/

# Run security tests
pytest tests/security/

# Check code style and format
ruff check .
ruff format .

# Type checking
mypy .
```

## Build System

- **Package Management**: pip with requirements.txt
- **Testing**: pytest with coverage reporting
- **Code Quality**: ruff for linting and formatting, mypy for type checking
- **Security**: Custom security validation framework with sandbox mode

## Architecture Patterns

- **Modular Design**: Clear separation between GUI, core logic, agents, tools, and integrations
- **Event-Driven**: Asynchronous communication between components
- **Plugin Architecture**: MCP protocol support for extensible tools
- **Configuration-Driven**: YAML-based settings for all components
- **Security-First**: Sandboxed operations with validation at every layer
