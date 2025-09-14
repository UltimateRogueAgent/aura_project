# LangChain Documentation

LangChain is a framework for developing applications powered by large language models (LLMs). It simplifies every stage of the LLM application lifecycle, offering open-source components and third-party integrations.

## Installation

### Basic Installation

```bash
pip install langchain
```

### With OpenAI Support

```bash
pip install langchain langchain-openai
```

### With Community Integrations

```bash
pip install langchain langchain-community
```

### Development Setup

```bash
# Clone and navigate to the repository
cd libs/langchain

# Install with uv (recommended)
uv sync

# Install pre-commit hooks
uv tool install pre-commit
pre-commit install
```

## Quick Start

### Basic LLM Usage

```python
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
import os

# Set API key
os.environ["OPENAI_API_KEY"] = "your-api-key"

# Initialize model
llm = ChatOpenAI(model="gpt-3.5-turbo")

# Send message
messages = [HumanMessage(content="Hello, how are you?")]
response = llm.invoke(messages)
print(response.content)
```

### Prompt Templates

```python
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# Define a prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert extraction algorithm. Only extract relevant information from the text."),
    MessagesPlaceholder("examples"),  # For few-shot examples
    ("human", "{text}")
])

# Use the template
formatted_prompt = prompt.format_messages(
    examples=[],
    text="Extract information from this text..."
)
```

### Chains and Runnables

```python
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

# Create a simple chain
prompt = ChatPromptTemplate.from_template("Tell me a joke about {topic}")
model = ChatOpenAI()
output_parser = StrOutputParser()

# Chain components together
chain = prompt | model | output_parser

# Run the chain
result = chain.invoke({"topic": "programming"})
print(result)
```

## Core Components

### 1. Models

- **Chat Models**: For conversational interfaces
- **LLMs**: For text completion
- **Embeddings**: For vector representations

```python
from langchain_openai import ChatOpenAI, OpenAI, OpenAIEmbeddings

# Chat model
chat_model = ChatOpenAI(model="gpt-4")

# Text completion model
llm = OpenAI(model="gpt-3.5-turbo-instruct")

# Embeddings
embeddings = OpenAIEmbeddings()
```

### 2. Prompts

- **PromptTemplate**: For simple string templates
- **ChatPromptTemplate**: For chat-based interactions
- **FewShotPromptTemplate**: For few-shot learning

```python
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate

# Simple template
template = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?"
)

# Few-shot template
examples = [
    {"input": "2 + 2", "output": "4"},
    {"input": "2 + 3", "output": "5"}
]

few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=PromptTemplate(
        input_variables=["input", "output"],
        template="Input: {input}\nOutput: {output}"
    ),
    input_variables=["input"],
    suffix="Input: {input}\nOutput:"
)
```

### 3. Output Parsers

```python
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field

# String parser
str_parser = StrOutputParser()

# JSON parser with schema
class Person(BaseModel):
    name: str = Field(description="person's name")
    age: int = Field(description="person's age")

json_parser = JsonOutputParser(pydantic_object=Person)
```

### 4. Vector Stores

```python
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

# Initialize embeddings
embeddings = OpenAIEmbeddings()

# Create vector store
vectorstore = Chroma.from_texts(
    texts=["Document 1 content", "Document 2 content"],
    embeddings=embeddings
)

# Search
results = vectorstore.similarity_search("query", k=2)
```

## Advanced Features

### Memory

```python
from langchain.memory import ConversationBufferMemory, ConversationBufferWindowMemory

# Buffer memory (keeps all messages)
memory = ConversationBufferMemory()

# Window memory (keeps last k messages)
window_memory = ConversationBufferWindowMemory(k=5)
```

### Agents and Tools

```python
from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# Create tools
search = DuckDuckGoSearchRun()
tools = [search]

# Create agent prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant"),
    ("user", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

# Create agent
agent = create_openai_functions_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Run agent
result = agent_executor.invoke({"input": "What's the weather like today?"})
```

### Document Loading and Processing

```python
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter

# Load documents
loader = TextLoader("path/to/document.txt")
documents = loader.load()

# Split documents
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)
```

## Testing and Development

### Running Tests

```bash
# Unit tests
make test
# or
uv run --group test pytest -n auto --disable-socket --allow-unix-socket tests/unit_tests

# Linting
make lint
# or
uv run --all-groups ruff check .
uv run --all-groups mypy . --cache-dir .mypy_cache

# Formatting
make format
# or
uv run --all-groups ruff format .
```

### Jupyter Development

```bash
# Run Jupyter with test dependencies
uv run --group test jupyter notebook
```

## Integration Examples

### With Anthropic

```python
from langchain_anthropic import ChatAnthropic

model = ChatAnthropic(model="claude-3-sonnet-20240229")
```

### With Google Vertex AI

```python
from langchain_google_vertexai import ChatVertexAI

model = ChatVertexAI(model_name="gemini-pro")
```

### With Local Models (llama-cpp)

```bash
# CPU only
pip install llama-cpp-python

# With CUDA support
CMAKE_ARGS="-DGGML_CUDA=on" FORCE_CMAKE=1 pip install llama-cpp-python

# With Metal support (macOS)
CMAKE_ARGS="-DLLAMA_METAL=on" FORCE_CMAKE=1 pip install llama-cpp-python
```

## Best Practices

1. **Environment Variables**: Always use environment variables for API keys
2. **Error Handling**: Implement proper error handling for API calls
3. **Rate Limiting**: Be mindful of API rate limits
4. **Caching**: Use caching for expensive operations
5. **Testing**: Write comprehensive tests for your chains and agents
6. **Documentation**: Follow Google-style docstrings for functions

## Common Patterns

### RAG (Retrieval-Augmented Generation)

```python
from langchain.chains import RetrievalQA

# Create retrieval chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever()
)

result = qa_chain.invoke({"query": "What is the main topic?"})
```

### Few-Shot Learning

```python
from langchain_core.example_selectors import SemanticSimilarityExampleSelector

# Create example selector
example_selector = SemanticSimilarityExampleSelector.from_examples(
    examples,
    embeddings,
    vectorstore,
    k=2
)

# Use in prompt
dynamic_prompt = FewShotPromptTemplate(
    example_selector=example_selector,
    example_prompt=example_prompt,
    input_variables=["input"]
)
```

This documentation provides a comprehensive overview of LangChain's capabilities for building LLM-powered applications.
