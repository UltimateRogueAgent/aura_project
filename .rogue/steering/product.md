# Product Overview

AURA (Autonomous Unit & Resource Arbitrator) is a desktop application that provides an intelligent multi-agent AI system through an intuitive chat interface. The system orchestrates specialized AI agents to handle complex user tasks through collaborative problem-solving.

## Core Concept

Users interact with AURA through a modern PyQt6 desktop interface, submitting tasks that are automatically analyzed and distributed among specialized agents:

- **Orchestrator**: Manages task breakdown and agent coordination using the rogue-v1-brain model
- **Researcher Agent**: Handles web research and information gathering using rogue-v1-agent model
- **Coder Agent**: Manages file operations, code creation, and terminal commands using rogue-v1-agent model
- **Designer Agent**: Plans solutions and system architecture using rogue-v1-agent model

## Key Features

- **Local AI Processing**: Uses Ollama for complete privacy and control over data
- **Long-term Memory**: ChromaDB vector storage for persistent knowledge across sessions
- **Web Integration**: Real-time web scraping and search capabilities via Playwright and DuckDuckGo
- **MCP Protocol Support**: Extensible tool system through Model Context Protocol servers
- **Modern GUI**: Dark/light themes with smooth animations and real-time progress visualization
- **Security-First**: Sandboxed operations with user confirmation for potentially dangerous actions

## Target Users

Developers, researchers, and power users who need an intelligent assistant that can:

- Research topics and gather information from the web
- Write and manage code files
- Plan and execute complex multi-step projects
- Maintain context and memory across work sessions
- Operate entirely offline with local models

## Communication Guidelines

- **User Responses**: Always respond to users in Polish language
- **Code Comments**: Use English for code documentation and technical terms
- **Configuration**: Polish labels in GUI, English for technical configuration keys
