# Requirements Document

AURA (Autonomous Unit & Resource Arbitrator) is a desktop application that enables communication with an AI agent orchestration system through a chat interface. The system consists of an Orchestrator managing a team of specialized agents (Researcher, Coder, Designer) who collaborate on executing complex user tasks. The application uses local LLM models (Ollama) and vector memory for storing long-term knowledge.

## Table of Contents

- [Requirements Document](#requirements-document)
  - [Table of Contents](#table-of-contents)
  - [Requirement 1](#requirement-1)
  - [Requirement 2](#requirement-2)
  - [Requirement 3](#requirement-3)
  - [Requirement 4](#requirement-4)
  - [Requirement 5](#requirement-5)
  - [Requirement 6](#requirement-6)
  - [Requirement 7](#requirement-7)
  - [Requirement 8](#requirement-8)
  - [Requirement 9](#requirement-9)
  - [Requirement 10](#requirement-10)
  - [Requirement 11](#requirement-11)
  - [Requirement 12](#requirement-12)

### **Requirement 1**

- _User Story:_

      As a user, I want to have a graphical desktop interface with chat, so I can communicate with the AURA system intuitively.

- _Acceptance Criteria:_

      1. WHEN the user starts the application THEN the system SHALL display a desktop window with chat interface
      2. WHEN the user types a command in the text field THEN the system SHALL display the message in the chat window
      3. WHEN the user presses Enter or the "Execute Task" button THEN the system SHALL begin processing the command
      4. WHEN the system is processing a task THEN the application SHALL display progress messages in real-time
      5. WHEN the task is completed THEN the system SHALL display the final result in the chat window

### **Requirement 2**

- _User Story:_

      As a user, I want the Orchestrator to analyze my commands and delegate tasks to appropriate agents, so complex problems are solved systematically.

- _Acceptance Criteria:_

      1. WHEN the user provides a complex task THEN the Orchestrator SHALL analyze it and break it down into smaller steps
      2. WHEN the Orchestrator identifies task steps THEN the system SHALL assign each step to the appropriate agent (Researcher, Coder, Designer)
      3. WHEN an agent completes its task THEN the result SHALL be passed back to the Orchestrator
      4. WHEN all steps are completed THEN the Orchestrator SHALL synthesize the final response
      5. IF the task requires information from the internet THEN the system SHALL delegate it to the Researcher agent

### **Requirement 3**

- _User Story:_

      As a user, I want the Researcher agent to be able to search and retrieve information from the internet, so the system has access to current data.

- _Acceptance Criteria:_

      1. WHEN the Researcher receives a search task THEN the agent SHALL use internet search tools
      2. WHEN the Researcher finds relevant pages THEN the system SHALL download and process their content
      3. WHEN content is downloaded THEN the system SHALL clean the text of unnecessary HTML elements
      4. WHEN text exceeds context limit THEN the system SHALL limit it to a maximum of 8000 characters
      5. WHEN the Researcher completes the search THEN results SHALL be passed to the Orchestrator

### **Requirement 4**

- _User Story:_

      As a user, I want the Coder agent to be able to create, modify and manage code files, so the system can implement programming solutions.

- _Acceptance Criteria:_

      1. WHEN the Coder receives a programming task THEN the agent SHALL be able to create new files
      2. WHEN the Coder works with files THEN the system SHALL enable reading, writing and listing files
      3. WHEN the Coder needs to execute system commands THEN the agent SHALL have access to terminal
      4. WHEN the Coder creates code THEN the system SHALL save it in the appropriate directory structure
      5. IF file operations fail THEN the system SHALL return error information

### **Requirement 5**

- _User Story:_

      As a user, I want the system to have long-term memory, so it can utilize previously acquired knowledge in future tasks.

- _Acceptance Criteria:_

      1. WHEN the system processes important information THEN data SHALL be saved in the vector database
      2. WHEN an agent needs information from the past THEN the system SHALL search long-term memory
      3. WHEN the system searches memory THEN results SHALL be sorted by relevance
      4. WHEN memory is updated THEN the system SHALL confirm data saving
      5. WHEN the application is restarted THEN long-term memory SHALL be preserved

### **Requirement 6**

- _User Story:_

      As a user, I want the system to use local LLM models through Ollama, so privacy and data control are maintained.

- _Acceptance Criteria:_

      1. WHEN the system starts THEN the application SHALL connect to the Ollama server
      2. WHEN the Orchestrator needs analysis THEN the system SHALL use the rogue-v1-brain model
      3. WHEN agents execute tasks THEN the system SHALL use the rogue-v1-agent model
      4. IF connection to Ollama fails THEN the system SHALL display an error message
      5. WHEN the model processes a query THEN the system SHALL handle the response asynchronously

### **Requirement 7**

- _User Story:_

      As a user, I want the application to operate securely, so my system is not exposed to harm.

- _Acceptance Criteria:_

      1. WHEN the Coder agent performs file operations THEN the system SHALL restrict access to safe directories
      2. WHEN an agent executes terminal commands THEN the system SHALL validate commands for security
      3. WHEN the system detects a potentially dangerous operation THEN the application SHALL ask for user confirmation
      4. WHEN a security error occurs THEN the system SHALL stop task execution
      5. IF the user does not confirm a risky operation THEN the system SHALL cancel the task

### **Requirement 8**

- _User Story:_

      As a user, I want the application to operate efficiently, so it doesn't overload my computer.

- _Acceptance Criteria:_

      1. WHEN the application processes tasks THEN the GUI SHALL remain responsive
      2. WHEN the system executes long-running operations THEN processing SHALL occur in separate threads
      3. WHEN an agent downloads data from the internet THEN the system SHALL limit the size of downloaded content
      4. WHEN context memory fills up THEN the system SHALL automatically manage its size
      5. WHEN the user closes the application THEN all processes SHALL be properly terminated

### **Requirement 9**

- _User Story:_

      As a user, I want the system to use specific Python libraries, so compatibility and functionality are ensured according to the project design.

- _Acceptance Criteria:_

      1. WHEN the system initializes THEN the application SHALL use CrewAI as the framework for agent orchestration
      2. WHEN the GUI is created THEN the system SHALL utilize PyQt6 for the desktop interface
      3. WHEN the Researcher agent searches for information THEN the system SHALL use playwright for advanced web browsing
      4. WHEN the system needs simpler searching THEN the application SHALL utilize duckduckgo-search
      5. WHEN the system parses HTML THEN the application SHALL use BeautifulSoup4
      6. WHEN the system connects to Ollama THEN the application SHALL utilize langchain-community and langchain-ollama
      7. WHEN the system manages vector memory THEN the application SHALL use ChromaDB
      8. WHEN the system needs environment variables THEN the application SHALL utilize python-dotenv

### **Requirement 10**

- _User Story:_

      As a user, I want the application to support tools from MCP (Model Context Protocol) servers, so agents' capabilities are extended with additional functionalities.

- _Acceptance Criteria:_

      1. WHEN the system starts THEN the application SHALL automatically detect and connect to available MCP servers
      2. WHEN an MCP server is available THEN the system SHALL load its tools and make them available to agents
      3. WHEN an agent needs to use an MCP tool THEN the system SHALL execute a call to the appropriate server
      4. WHEN an MCP tool returns a result THEN the system SHALL process the response and pass it to the agent
      5. IF an MCP server is not available THEN the system SHALL continue working with available local tools

### **Requirement 11**

- _User Story:_

      As a user, I want the application to be modular and easy to navigate, so I can easily expand and modify the system.

- _Acceptance Criteria:_

      1. WHEN a developer reviews the code THEN the project structure SHALL be logically divided into modules
      2. WHEN a developer wants to add a new agent THEN the system SHALL enable easy addition by creating a new module
      3. WHEN a developer wants to add a new tool THEN the system SHALL allow adding it in the dedicated tools module
      4. WHEN a developer modifies functionality THEN changes SHALL be isolated in appropriate modules
      5. WHEN the system starts THEN modules SHALL be automatically detected and loaded

### **Requirement 12**

- _User Story:_

      As a user, I want to have a central configuration file, so I can easily manage all application settings in one place.

- _Acceptance Criteria:_

      1. WHEN the application starts THEN the system SHALL load all settings from the central configuration file
      2. WHEN the user changes a setting in the configuration file THEN the change SHALL be automatically applied throughout the application
      3. WHEN a module needs a configuration parameter THEN the system SHALL automatically provide the value from central configuration
      4. WHEN a new module is added THEN its settings SHALL be added to the central configuration file
      5. IF the configuration file does not exist THEN the system SHALL create a default file with basic settings
