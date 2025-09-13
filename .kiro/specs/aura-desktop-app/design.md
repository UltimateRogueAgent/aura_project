# Design Document - AURA Desktop Application

AURA (Autonomous Unit & Resource Arbitrator) to modułowa aplikacja desktopowa zbudowana w architekturze wieloagentowej, która umożliwia użytkownikom komunikację z systemem orkiestracji agentów AI poprzez intuicyjny interfejs czatu. System wykorzystuje CrewAI do zarządzania agentami, Ollama do obsługi lokalnych modeli LLM, oraz ChromaDB do pamięci długoterminowej.

## Architecture

```mermaid
graph TB
    subgraph "Desktop Application"
        GUI[PyQt6 GUI Layer]
        CONFIG[Configuration Manager]
        CORE[Core Application Logic]
    end

    subgraph "Agent Orchestration"
        ORCH[Orchestrator - rogue-v1-brain]
        CREW[CrewAI Framework]
        RESEARCHER[Researcher Agent]
        CODER[Coder Agent]
        DESIGNER[Designer Agent]
    end

    subgraph "External Services"
        OLLAMA[Ollama LLM Server]
        MCP[MCP Servers]
        WEB[Web Resources]
    end

    subgraph "Storage"
        CHROMA[ChromaDB Vector Store]
        FILES[File System]
    end

    GUI --> CORE
    CORE --> CONFIG
    CORE --> CREW
    CREW --> ORCH
    CREW --> RESEARCHER
    CREW --> CODER
    CREW --> DESIGNER

    ORCH --> OLLAMA
    RESEARCHER --> OLLAMA
    CODER --> OLLAMA
    DESIGNER --> OLLAMA

    RESEARCHER --> WEB
    RESEARCHER --> MCP
    CODER --> FILES
    CODER --> MCP
    DESIGNER --> MCP

    CREW --> CHROMA
```

## Modular Structure

```text
aura_project/
├── config/
│   ├── __init__.py
│   ├── settings.py          # Centralny manager konfiguracji
│   ├── default_config.yaml  # Domyślne ustawienia
│   └── themes/              # Motywy GUI
│       ├── dark.yaml
│       ├── light.yaml
│       └── custom.yaml
├── core/
│   ├── __init__.py
│   ├── application.py       # Główna logika aplikacji
│   └── event_manager.py     # System zdarzeń
├── agents/
│   ├── __init__.py
│   ├── base_agent.py        # Bazowa klasa agenta
│   ├── researcher.py        # Agent Researcher
│   ├── coder.py            # Agent Coder
│   └── designer.py         # Agent Designer
├── tools/
│   ├── __init__.py
│   ├── base_tool.py        # Bazowa klasa narzędzia
│   ├── file_tools.py       # Narzędzia do plików
│   ├── web_tools.py        # Narzędzia internetowe
│   └── mcp_tools.py        # Integracja z MCP
├── memory/
│   ├── __init__.py
│   ├── vector_store.py     # ChromaDB integration
│   └── memory_manager.py   # Manager pamięci
├── gui/
│   ├── __init__.py
│   ├── main_window.py      # Główne okno
│   ├── chat_widget.py      # Widget czatu
│   ├── settings_panel.py   # Zaawansowany panel ustawień
│   ├── theme_manager.py    # Manager motywów
│   ├── animation_manager.py # Manager animacji
│   ├── components/         # Komponenty UI
│   │   ├── __init__.py
│   │   ├── progress_widgets.py
│   │   ├── agent_status.py
│   │   ├── tool_indicators.py
│   │   ├── notification_system.py
│   │   └── modern_controls.py
│   └── styles/             # Style CSS/QSS
│       ├── dark_theme.qss
│       ├── light_theme.qss
│       └── animations.qss
├── integrations/
│   ├── __init__.py
│   ├── ollama_client.py    # Klient Ollama
│   └── mcp_client.py       # Klient MCP
├── utils/
│   ├── __init__.py
│   ├── logging.py          # System logowania
│   └── validators.py       # Walidatory
├── assets/                 # Zasoby graficzne
│   ├── icons/
│   ├── fonts/
│   └── animations/
├── main.py                 # Punkt wejścia aplikacji
└── requirements.txt        # Zależności
```

## Components and Interfaces

### 1. Configuration Manager

**Lokalizacja:** `config/settings.py`

**Odpowiedzialność:** Centralne zarządzanie wszystkimi ustawieniami aplikacji

**Kluczowe funkcje:**

- Ładowanie konfiguracji z pliku YAML
- Automatyczne wykrywanie zmian w konfiguracji
- Walidacja ustawień
- Dostarczanie ustawień do wszystkich modułów

**Interface:**

```python
class ConfigManager:
    def get(self, key: str, default=None) -> Any
    def set(self, key: str, value: Any) -> None
    def reload(self) -> None
    def validate(self) -> bool
    def get_section(self, section: str) -> Dict[str, Any]
```

---

### 2. Core Application Logic

**Lokalizacja:** `core/application.py`

**Odpowiedzialność:** Główna logika aplikacji, koordynacja między komponentami

**Kluczowe funkcje:**

- Inicjalizacja wszystkich komponentów
- Zarządzanie cyklem życia aplikacji
- Koordynacja komunikacji między warstwami
- Obsługa błędów na poziomie aplikacji

**Interface:**

```python
class AuraApplication:
    def initialize(self) -> None
    def start(self) -> None
    def shutdown(self) -> None
    def process_user_request(self, request: str) -> str
    def get_status(self) -> Dict[str, Any]
```

---

### 3. Agent System

**Lokalizacja:** `agents/`

**Odpowiedzialność:** Implementacja systemu agentów z wykorzystaniem CrewAI

**Architektura agentów:**

#### Base Agent

```python
class BaseAgent:
    def __init__(self, config: Dict[str, Any])
    def setup_tools(self) -> List[Tool]
    def execute_task(self, task: Task) -> TaskResult
    def get_capabilities(self) -> List[str]
```

#### Orchestrator (Manager w CrewAI)

- **Model:** rogue-v1-brain
- **Rola:** Zarządzanie i koordynacja innych agentów
- **Narzędzia:** Memory tools, MCP tools
- **Proces:** Hierarchical process w CrewAI

#### Researcher Agent

- **Model:** rogue-v1-agent
- **Rola:** Wyszukiwanie i agregacja informacji
- **Narzędzia:** Web scraping, search engines, MCP brave search, other MCP tools
- **Specjalizacja:** Analiza danych, research internetowy

#### Coder Agent

- **Model:** rogue-v1-agent
- **Rola:** Tworzenie i zarządzanie kodem
- **Narzędzia:** File system, terminal, MCP context7, other MCP tools
- **Specjalizacja:** Programowanie, debugowanie, zarządzanie plikami

#### Designer Agent

- **Model:** rogue-v1-agent
- **Rola:** Planowanie i projektowanie rozwiązań
- **Narzędzia:** Memory tools, MCP tools
- **Specjalizacja:** Architektura systemu, planowanie zadań

---

### 4. Tool System

**Lokalizacja:** `tools/`

**Odpowiedzialność:** Modułowy system narzędzi dla agentów

**Architektura narzędzi:**

#### Base Tool Interface

```python
class BaseTool:
    def __init__(self, config: Dict[str, Any])
    def execute(self, *args, **kwargs) -> ToolResult
    def validate_input(self, *args, **kwargs) -> bool
    def get_description(self) -> str
    def get_schema(self) -> Dict[str, Any]
```

#### File Tools

- File system operations (read, write, list, copy, delete, find, move, etc.)
- Directory management
- Security validation
- Path sanitization

#### Web Tools

- Playwright realtime automation, web scraping
- DuckDuckGo search
- Web content extraction and processing
- Content cleaning and processing
- Rate limiting and caching

#### MCP Tools

- Dynamic MCP server discovery
- Tool registration and execution
- Error handling and fallbacks
- Security validation

---

### 5. Memory System

**Lokalizacja:** `memory/`

**Odpowiedzialność:** Zarządzanie pamięcią długoterminową i krótkoterminową

**Komponenty:**

#### Vector Store Manager

```python
class VectorStoreManager:
    def __init__(self, config: Dict[str, Any])
    def add_memory(self, text: str, metadata: Dict = None) -> str
    def search_memory(self, query: str, k: int = 5) -> List[MemoryResult]
    def delete_memory(self, memory_id: str) -> bool
    def get_statistics(self) -> Dict[str, Any]
```

#### Memory Manager

- Automatyczne zarządzanie kontekstem
- Kompresja długich konwersacji
- Kategoryzacja wspomnień
- Garbage collection dla starych danych

---

### 6. GUI Layer

**Lokalizacja:** `gui/`

**Odpowiedzialność:** Nowoczesny interfejs użytkownika z wykorzystaniem PyQt6

**Architektura GUI:**

#### Main Window

- Modern dark theme with customizable colors
- Smooth animations and transitions
- Responsive layout management
- Advanced menu system with icons
- Animated status bar with progress indicators
- Window state management with smooth resizing

#### Chat Widget

- Real-time message display with typing animations
- Rich text formatting with syntax highlighting
- Tool usage indicators with animated icons
- Progress bars for long-running operations
- Agent activity visualization
- Message bubbles with smooth fade-in effects
- Auto-scroll with smooth scrolling animation

#### Advanced Settings Panel

- Tabbed interface for different setting categories
- Real-time configuration validation
- Live preview of changes
- Search functionality for settings
- Import/export configuration profiles
- Reset to defaults with confirmation dialogs
- Tooltips and help text for all options

#### Components

- Animated progress indicators with smooth transitions
- Modern toggle switches and sliders
- Floating action buttons with hover effects
- Notification system with slide-in animations
- Agent status cards with real-time updates
- Interactive log viewers with filtering
- Collapsible panels with smooth expand/collapse
- Loading spinners and skeleton screens

#### Theme System

```python
class ThemeManager:
    def load_theme(self, theme_name: str) -> None
    def apply_animations(self, widget: QWidget) -> None
    def get_color_palette(self) -> Dict[str, str]
    def set_custom_colors(self, colors: Dict[str, str]) -> None
```

#### Animation System

```python
class AnimationManager:
    def fade_in(self, widget: QWidget, duration: int = 300) -> None
    def slide_in(self, widget: QWidget, direction: str = "left") -> None
    def smooth_scroll(self, scroll_area: QScrollArea, target: int) -> None
    def progress_animation(self, progress_bar: QProgressBar) -> None
```

---

### 7. Integration Layer

**Lokalizacja:** `integrations/`

**Odpowiedzialność:** Integracja z zewnętrznymi serwisami

#### Ollama Client

```python
class OllamaClient:
    def __init__(self, config: Dict[str, Any])
    def check_connection(self) -> bool
    def list_models(self) -> List[str]
    def generate(self, model: str, prompt: str) -> str
    def get_model_info(self, model: str) -> Dict[str, Any]
```

#### MCP Client

```python
class MCPClient:
    def __init__(self, config: Dict[str, Any])
    def discover_servers(self) -> List[MCPServer]
    def connect_to_server(self, server_config: Dict) -> MCPConnection
    def list_tools(self, server: str) -> List[MCPTool]
    def execute_tool(self, server: str, tool: str, params: Dict) -> Any
```

## Data Models

### Configuration Schema

---

```yaml
# default_config.yaml
application:
  name: "AURA"
  version: "1.0.0"
  debug: false
  log_level: "INFO"

ollama:
  host: "localhost"
  port: 11434
  orchestrator_model: "rogue-v1-brain"
  agent_model: "rogue-v1-agent"
  timeout: 30

memory:
  vector_store:
    type: "chromadb"
    path: "./data/chroma_db"
    collection_name: "aura_memory"
  context_window: 8000
  max_memories: 10000

agents:
  researcher:
    enabled: true
    max_search_results: 10
    web_timeout: 30
  coder:
    enabled: true
    safe_mode: true
    allowed_paths: ["./workspace", "./projects"]
  designer:
    enabled: true
    planning_depth: 3

mcp:
  enabled: true
  auto_discover: true
  servers: []
  timeout: 15

gui:
  theme:
    name: "dark"
    primary_color: "#2D3748"
    secondary_color: "#4A5568"
    accent_color: "#63B3ED"
    text_color: "#E2E8F0"
    background_color: "#1A202C"
    success_color: "#48BB78"
    warning_color: "#ED8936"
    error_color: "#F56565"
  window:
    size: [1400, 900]
    min_size: [800, 600]
    resizable: true
    center_on_screen: true
  fonts:
    primary: "Segoe UI"
    monospace: "Consolas"
    size: 12
    scaling: 1.0
  animations:
    enabled: true
    duration: 300
    easing: "ease_in_out"
  chat:
    auto_scroll: true
    smooth_scrolling: true
    show_timestamps: true
    show_agent_avatars: true
    typing_indicator: true
    message_animations: true
  settings:
    show_advanced: false
    live_preview: true
    search_enabled: true
    categories_expanded: false

security:
  sandbox_mode: true
  require_confirmation: true
  allowed_operations: ["read", "write", "search"]
```

## Task Flow Model

```python
@dataclass
class TaskRequest:
    id: str
    user_input: str
    timestamp: datetime
    priority: int = 1

@dataclass
class TaskStep:
    id: str
    agent: str
    description: str
    dependencies: List[str]
    status: TaskStatus
    result: Optional[str] = None

@dataclass
class TaskResult:
    task_id: str
    success: bool
    result: str
    execution_time: float
    agent_logs: List[str]
```

## Memory Model

```python
@dataclass
class MemoryEntry:
    id: str
    content: str
    metadata: Dict[str, Any]
    timestamp: datetime
    category: str
    relevance_score: float = 0.0

@dataclass
class MemorySearchResult:
    entry: MemoryEntry
    similarity_score: float
    context: str
```

## Error Handling

### Error Categories

1. **Configuration Errors**

   - Invalid configuration files
   - Missing required settings
   - Type validation errors

2. **Connection Errors**

   - Ollama server unavailable
   - MCP server connection failures
   - Network timeouts

3. **Agent Execution Errors**

   - Task execution failures
   - Tool execution errors
   - Model response errors

4. **Security Errors**
   - Unauthorized file access
   - Dangerous command execution
   - MCP security violations

### Error Handling Strategy

```python
class ErrorHandler:
    def handle_configuration_error(self, error: ConfigError) -> None
    def handle_connection_error(self, error: ConnectionError) -> None
    def handle_agent_error(self, error: AgentError) -> None
    def handle_security_error(self, error: SecurityError) -> None
    def log_error(self, error: Exception, context: Dict) -> None
```

### Recovery Mechanisms

- **Graceful Degradation:** System continues with limited functionality
- **Automatic Retry:** Configurable retry logic for transient errors
- **Fallback Options:** Alternative tools/agents when primary fails
- **User Notification:** Clear error messages with suggested actions

## Testing Strategy

### Unit Testing

- **Coverage Target:** 90%+
- **Framework:** pytest
- **Mock Strategy:** Mock external dependencies (Ollama, MCP, web)
- **Test Categories:**
  - Configuration management
  - Agent logic
  - Tool execution
  - Memory operations
  - GUI components

### Integration Testing

- **Agent Coordination:** Test CrewAI workflow execution
- **External Services:** Test Ollama and MCP integration
- **End-to-End:** Complete user request processing
- **Performance:** Response time and resource usage

### Security Testing

- **Input Validation:** Test malicious input handling
- **File System Access:** Test sandbox restrictions
- **Command Execution:** Test dangerous command prevention
- **MCP Security:** Test MCP tool validation

### Test Structure

```text
tests/
├── unit/
│   ├── test_config.py
│   ├── test_agents.py
│   ├── test_tools.py
│   ├── test_memory.py
│   └── test_gui.py
├── integration/
│   ├── test_crew_workflow.py
│   ├── test_ollama_integration.py
│   └── test_mcp_integration.py
├── security/
│   ├── test_input_validation.py
│   ├── test_file_security.py
│   └── test_command_security.py
└── fixtures/
    ├── sample_configs/
    ├── mock_responses/
    └── test_data/
```

## Performance Considerations

### Optimization Strategies

1. **Asynchronous Processing**

   - GUI remains responsive during long operations
   - Parallel agent execution where possible
   - Background memory indexing

2. **Memory Management**

   - Configurable context window limits
   - Automatic memory cleanup
   - Efficient vector storage

3. **Caching**

   - Web scraping results
   - Model responses for similar queries
   - MCP tool schemas

4. **Resource Monitoring**
   - CPU and memory usage tracking
   - Model loading optimization
   - Connection pooling

### Scalability Design

- **Modular Architecture:** Easy to add new agents/tools
- **Configuration-Driven:** Behavior modification without code changes
- **Plugin System:** Support for external extensions
- **Distributed Processing:** Future support for remote agents

## Security Architecture

### Security Layers

1. **Input Validation**

   - Sanitize all user inputs
   - Validate file paths and commands
   - Check MCP tool parameters

2. **Sandbox Environment**

   - Restrict file system access
   - Limit command execution
   - Isolate agent operations

3. **Permission System**

   - User confirmation for risky operations
   - Configurable security levels
   - Audit logging

4. **Data Protection**
   - Local data storage only
   - Encrypted sensitive configurations
   - Secure memory handling

### Security Configuration

```yaml
security:
  sandbox_mode: true
  require_confirmation: true
  allowed_paths:
    - "./workspace"
    - "./projects"
  blocked_commands:
    - "rm -rf"
    - "del /f /s /q"
    - "format"
  mcp_validation: true
  audit_logging: true
```
