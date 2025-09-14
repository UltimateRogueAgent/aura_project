# CrewAI Documentation

CrewAI is a Python framework for orchestrating autonomous AI agents, offering a lean, fast, and flexible approach to building AI-powered applications with granular control and scalability.

## Installation

```bash
pip install crewai
```

For additional tools:

```bash
pip install 'crewai[tools]'
```

## Quick Start

### Basic Agent and Task Setup

```python
from crewai import Agent, Task, Crew

# Create an agent
researcher = Agent(
    role='Market Research Analyst',
    goal='Provide up-to-date market analysis of the AI industry',
    backstory='An expert analyst with a keen eye for market trends.',
    verbose=True
)

# Define a task
research = Task(
    description='Research the latest trends in the AI industry and provide a summary.',
    expected_output='A summary of the top 3 trending developments in the AI industry with a unique perspective on their significance.',
    agent=researcher
)

# Create and run crew
crew = Crew(
    agents=[researcher],
    tasks=[research],
    verbose=True
)

result = crew.kickoff()
print(result)
```

### Using Tools with Agents

```python
from crewai import Agent, Task, Crew
from crewai_tools import (
    DirectoryReadTool,
    FileReadTool,
    SerperDevTool,
    WebsiteSearchTool
)

# Instantiate tools
docs_tool = DirectoryReadTool(directory='./blog-posts')
file_tool = FileReadTool()
search_tool = SerperDevTool()
web_rag_tool = WebsiteSearchTool()

# Create agents with tools
researcher = Agent(
    role='Market Research Analyst',
    goal='Provide up-to-date market analysis of the AI industry',
    backstory='An expert analyst with a keen eye for market trends.',
    tools=[search_tool, web_rag_tool],
    verbose=True
)

writer = Agent(
    role='Content Writer',
    goal='Craft engaging blog posts about the AI industry',
    backstory='A skilled writer with a passion for technology.',
    tools=[docs_tool, file_tool],
    verbose=True
)
```

## CLI Commands

### Create New Project

```bash
crewai create crew project-name
```

### Install Dependencies

```bash
crewai install
```

### Run Project

```bash
crewai run
```

## Key Features

- **Multi-Agent Orchestration**: Coordinate multiple AI agents working together
- **Tool Integration**: Extensive library of tools for web scraping, file operations, search, etc.
- **Flexible Workflows**: Sequential and hierarchical process management
- **Planning Capabilities**: Enable agents to plan their approach to complex tasks
- **Memory System**: Long-term memory for context retention across sessions

## Advanced Features

### Flows

CrewAI Flows allow you to create complex, stateful workflows:

```python
from crewai.flow.flow import Flow, listen, start

class ContentProductionFlow(Flow):
    @start()
    def initialize_project(self):
        self.state.topic = "Sustainable Investing"
        self.state.target_audience = "Millennial Investors"
        self.state.content_type = "Blog Post"
        return "Project initialized"
```

### Enterprise Integration

CrewAI supports enterprise integrations like Zendesk:

```python
from crewai_tools import CrewaiEnterpriseTools

enterprise_tools = CrewaiEnterpriseTools(
    enterprise_token="your_enterprise_token"
)

zendesk_agent = Agent(
    role="Support Manager",
    goal="Manage customer support tickets",
    tools=[enterprise_tools]
)
```

## Common Tools

### File and Document Processing

- `FileReadTool`: Read file contents
- `PDFSearchTool`: Search within PDF documents
- `JSONSearchTool`: Process JSON data
- `DirectoryReadTool`: Read directory contents

### Web Scraping and Search

- `ScrapeWebsiteTool`: Basic web scraping
- `FirecrawlScrapeWebsiteTool`: Advanced web scraping
- `SeleniumScrapingTool`: Browser automation
- `SerperDevTool`: Google search integration
- `WebsiteSearchTool`: Website-specific search

### Database Integration

- `NL2SQLTool`: Natural language to SQL conversion
- `WeaviateVectorSearchTool`: Vector database search

## Best Practices

1. **Define Clear Roles**: Give each agent a specific role and clear goals
2. **Use Appropriate Tools**: Match tools to agent capabilities and tasks
3. **Enable Planning**: Use `planning=True` for complex multi-step tasks
4. **Verbose Output**: Enable verbose mode for debugging and monitoring
5. **Task Dependencies**: Structure tasks with clear dependencies and expected outputs

## Environment Setup

```bash
# Required environment variables
export OPENAI_API_KEY="your-openai-key"
export SERPER_API_KEY="your-serper-key"  # For search functionality
```

## Project Structure

```text
my_project/
├── src/
│   └── my_project/
│       ├── __init__.py
│       ├── main.py
│       ├── crew.py
│       └── config/
│           ├── agents.yaml
│           └── tasks.yaml
├── pyproject.toml
└── README.md
```

This documentation covers the essential aspects of CrewAI for building multi-agent AI systems with collaborative capabilities.
