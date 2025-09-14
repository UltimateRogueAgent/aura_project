# Ollama Python Documentation

The Ollama Python library provides an easy way to integrate Python 3.8+ projects with Ollama, supporting chat, generation, streaming, and custom client configurations.

## Installation

```bash
pip install ollama
```

## Quick Start

### Basic Usage

```python
import ollama

# Simple generation
response = ollama.generate(model='llama2', prompt='Why is the sky blue?')
print(response['response'])

# Chat interface
response = ollama.chat(
    model='llama2',
    messages=[
        {
            'role': 'user',
            'content': 'Hello, how are you?',
        },
    ],
)
print(response['message']['content'])
```

### Using Custom Client

```python
from ollama import Client

client = Client(host='http://localhost:11434')

response = client.chat(
    model='llama2',
    messages=[
        {
            'role': 'user',
            'content': 'Hello!',
        },
    ],
)
print(response['message']['content'])
```

## Core Functions

### Chat Interface

```python
import ollama

# Basic chat
response = ollama.chat(
    model='llama2',
    messages=[
        {
            'role': 'system',
            'content': 'You are a helpful assistant.',
        },
        {
            'role': 'user',
            'content': 'Explain quantum computing',
        },
    ],
)

print(response['message']['content'])
```

### Streaming Chat

```python
import ollama

stream = ollama.chat(
    model='llama2',
    messages=[
        {
            'role': 'user',
            'content': 'Tell me a story',
        },
    ],
    stream=True,
)

for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)
```

### Text Generation

```python
import ollama

# Basic generation
response = ollama.generate(
    model='llama2',
    prompt='Write a haiku about programming',
)
print(response['response'])

# Streaming generation
stream = ollama.generate(
    model='llama2',
    prompt='Explain machine learning',
    stream=True,
)

for chunk in stream:
    print(chunk['response'], end='', flush=True)
```

## Model Management

### List Models

```python
import ollama

models = ollama.list()
for model in models['models']:
    print(f"- {model['name']} (Size: {model['size'] // (1024*1024)} MB)")
```

### Pull Models

```python
import ollama

# Pull a model
ollama.pull('llama2')

# Pull with progress (requires tqdm)
try:
    response = ollama.pull('llama2', stream=True)
    for chunk in response:
        print(chunk['status'], end=' ', flush=True)
    print("\nModel pulled successfully.")
except Exception as e:
    print(f"Error pulling model: {e}")
```

### Show Model Details

```python
import ollama

model_info = ollama.show('llama2')
print(f"Name: {model_info['name']}")
print(f"Size: {model_info['size']} bytes")
print(f"Parameters: {model_info['details']['parameter_size']}")
print(f"Family: {model_info['details']['family']}")
```

### Create Custom Models

```python
import ollama

# Create from Modelfile
modelfile = '''
FROM llama2
SYSTEM "You are a helpful coding assistant."
PARAMETER temperature 0.7
'''

ollama.create(model='my-coding-assistant', modelfile=modelfile)
```

### Delete Models

```python
import ollama

ollama.delete('model-name')
```

## Advanced Features

### Function Calling / Tools

```python
import ollama

response = ollama.chat(
    model='llama2',
    messages=[
        {
            'role': 'user',
            'content': 'What is the weather in San Francisco?',
        }
    ],
    tools=[
        {
            'type': 'function',
            'function': {
                'name': 'get_weather',
                'description': 'Get the weather for a location',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'location': {
                            'type': 'string',
                            'description': 'The location to get weather for',
                        }
                    },
                    'required': ['location'],
                },
            }
        }
    ]
)

# Check if model wants to call a function
if 'tool_calls' in response['message']:
    for tool_call in response['message']['tool_calls']:
        function_name = tool_call['function']['name']
        arguments = tool_call['function']['arguments']
        print(f"Model wants to call: {function_name} with {arguments}")
```

### Multiple Tools Example

```python
import ollama

response = ollama.chat(
    model='llama2',
    messages=[
        {
            'role': 'user',
            'content': 'What is the weather in Paris and what is the capital of France?',
        }
    ],
    tools=[
        {
            'type': 'function',
            'function': {
                'name': 'get_weather',
                'description': 'Get the weather for a location',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'location': {
                            'type': 'string',
                            'description': 'The location to get weather for',
                        }
                    },
                    'required': ['location'],
                },
            }
        },
        {
            'type': 'function',
            'function': {
                'name': 'get_capital',
                'description': 'Get the capital of a country',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'country': {
                            'type': 'string',
                            'description': 'The country to get the capital for',
                        }
                    },
                    'required': ['country'],
                },
            }
        }
    ]
)

print(response['message']['tool_calls'])
```

### Embeddings

```python
import ollama

# Generate embeddings
response = ollama.embeddings(
    model='llama2',
    prompt='This is a test sentence for embedding.',
)

print(f"Embedding dimension: {len(response['embedding'])}")
print(f"First 5 values: {response['embedding'][:5]}")
```

### Using Client Class

```python
from ollama import Client

client = Client('http://localhost:11434')

# All the same methods are available on the client
response = client.chat(
    model='llama2',
    messages=[{'role': 'user', 'content': 'Hello!'}]
)

# Generate embeddings
embeddings = client.embeddings(
    model='llama2',
    prompt='Text to embed'
)
```

## Configuration Options

### Model Parameters

```python
import ollama

response = ollama.generate(
    model='llama2',
    prompt='Tell me about AI',
    options={
        'temperature': 0.7,      # Creativity (0.0 to 1.0)
        'top_p': 0.9,           # Nucleus sampling
        'top_k': 40,            # Top-k sampling
        'repeat_penalty': 1.1,   # Repetition penalty
        'num_predict': 100,      # Max tokens to generate
        'num_ctx': 2048,        # Context window size
        'stop': ['\n'],         # Stop sequences
    }
)
```

### Keep Alive

```python
import ollama

# Keep model loaded for 5 minutes
response = ollama.generate(
    model='llama2',
    prompt='Hello',
    keep_alive='5m'
)

# Keep model loaded indefinitely
response = ollama.generate(
    model='llama2',
    prompt='Hello',
    keep_alive=-1
)

# Unload model immediately after use
response = ollama.generate(
    model='llama2',
    prompt='Hello',
    keep_alive=0
)
```

## System Status

### Check Running Models

```python
import ollama

status = ollama.ps()
if not status['models']:
    print("No models are currently running.")
else:
    for model_info in status['models']:
        print(f"Model: {model_info['name']}")
        print(f"Size: {model_info['size_vram']} bytes in VRAM")
        print(f"Until: {model_info['expires_at']}")
```

### Server Health Check

```python
from ollama import Client

client = Client('http://localhost:11434')

try:
    # This will raise an exception if server is not reachable
    models = client.list()
    print("Ollama server is running")
except Exception as e:
    print(f"Ollama server is not accessible: {e}")
```

## Async Support

### Async Client

```python
import asyncio
import ollama

async def main():
    # Async chat
    response = await ollama.AsyncClient().chat(
        model='llama2',
        messages=[
            {
                'role': 'user',
                'content': 'Hello async world!',
            },
        ],
    )
    print(response['message']['content'])

    # Async streaming
    async for part in await ollama.AsyncClient().chat(
        model='llama2',
        messages=[
            {
                'role': 'user',
                'content': 'Tell me a story',
            },
        ],
        stream=True,
    ):
        print(part['message']['content'], end='', flush=True)

asyncio.run(main())
```

## Error Handling

### Basic Error Handling

```python
import ollama

try:
    response = ollama.chat(
        model='nonexistent-model',
        messages=[{'role': 'user', 'content': 'Hello'}]
    )
except ollama.ResponseError as e:
    print(f"Ollama error: {e.error}")
    if e.status_code:
        print(f"Status code: {e.status_code}")
except Exception as e:
    print(f"Other error: {e}")
```

### Connection Error Handling

```python
from ollama import Client
import requests

try:
    client = Client(host='http://localhost:11434')
    response = client.list()
except requests.exceptions.ConnectionError:
    print("Cannot connect to Ollama server. Is it running?")
except Exception as e:
    print(f"Error: {e}")
```

## Best Practices

### Model Loading Strategy

```python
import ollama

# Pre-load model to avoid first-request delay
ollama.generate(model='llama2', prompt='', keep_alive='10m')

# Use the model
response = ollama.chat(
    model='llama2',
    messages=[{'role': 'user', 'content': 'Hello!'}]
)
```

### Conversation Management

```python
import ollama

class ChatSession:
    def __init__(self, model='llama2', system_prompt=None):
        self.model = model
        self.messages = []
        if system_prompt:
            self.messages.append({
                'role': 'system',
                'content': system_prompt
            })

    def chat(self, user_message):
        self.messages.append({
            'role': 'user',
            'content': user_message
        })

        response = ollama.chat(
            model=self.model,
            messages=self.messages
        )

        assistant_message = response['message']['content']
        self.messages.append({
            'role': 'assistant',
            'content': assistant_message
        })

        return assistant_message

    def clear_history(self):
        # Keep system message if it exists
        system_messages = [msg for msg in self.messages if msg['role'] == 'system']
        self.messages = system_messages

# Usage
session = ChatSession(
    model='llama2',
    system_prompt='You are a helpful coding assistant.'
)

response1 = session.chat('How do I create a Python list?')
response2 = session.chat('Can you show me an example?')
```

### Batch Processing

```python
import ollama

def process_batch(prompts, model='llama2'):
    results = []
    for prompt in prompts:
        try:
            response = ollama.generate(model=model, prompt=prompt)
            results.append(response['response'])
        except Exception as e:
            results.append(f"Error: {e}")
    return results

prompts = [
    "What is Python?",
    "Explain machine learning",
    "How does the internet work?"
]

results = process_batch(prompts)
for i, result in enumerate(results):
    print(f"Prompt {i+1}: {result[:100]}...")
```

## Common Use Cases

### Code Generation

```python
import ollama

def generate_code(description, language='python'):
    prompt = f"Write {language} code for: {description}"

    response = ollama.generate(
        model='codellama',  # Use a code-specific model if available
        prompt=prompt,
        options={'temperature': 0.2}  # Lower temperature for more deterministic code
    )

    return response['response']

code = generate_code("a function that calculates fibonacci numbers")
print(code)
```

### Text Summarization

```python
import ollama

def summarize_text(text, max_length=100):
    prompt = f"Summarize the following text in {max_length} words or less:\n\n{text}"

    response = ollama.generate(
        model='llama2',
        prompt=prompt,
        options={'temperature': 0.3}
    )

    return response['response']

long_text = "Your long text here..."
summary = summarize_text(long_text)
print(summary)
```

### Question Answering

```python
import ollama

def answer_question(context, question):
    prompt = f"""Context: {context}

Question: {question}

Answer based on the context provided:"""

    response = ollama.generate(
        model='llama2',
        prompt=prompt,
        options={'temperature': 0.1}
    )

    return response['response']

context = "Python is a high-level programming language..."
question = "What is Python?"
answer = answer_question(context, question)
print(answer)
```

This documentation covers the essential features of the Ollama Python library for integrating local LLM capabilities into Python applications.
