# ChromaDB Documentation

Chroma is the open-source embedding database, offering the fastest way to build LLM apps with memory for Python and JavaScript.

## Installation

### Python

```bash
pip install chromadb
```

```bash
poetry add chromadb
```

```bash
uv pip install chromadb
```

### JavaScript/TypeScript

```bash
npm install chromadb @chroma-core/default-embed
```

```bash
pnpm add chromadb @chroma-core/default-embed
```

```bash
yarn add chromadb @chroma-core/default-embed
```

```bash
bun add chromadb @chroma-core/default-embed
```

## Quick Start

### Python code

```python
import chromadb

# Create a client
chroma_client = chromadb.Client()

# Create a collection
collection = chroma_client.create_collection(name="my_collection")

# Add documents
collection.add(
    documents=["This is document 1", "This is document 2"],
    ids=["doc1", "doc2"]
)

# Query the collection
results = collection.query(
    query_texts=["This is a query"],
    n_results=1
)

print(results)
```

### TypeScript/JavaScript

```typescript
import { ChromaClient } from "chromadb";

// Create a client
const client = new ChromaClient();

// Create a collection
const collection = await client.createCollection({ name: "my_documents" });

// Add documents
await collection.add({
  documents: ["This is document 1", "This is document 2"],
  ids: ["doc1", "doc2"],
});

// Query the collection
const results = await collection.query({
  queryTexts: ["This is a query"],
  nResults: 1,
});

console.log(results);
```

## Running ChromaDB Server

### Using CLI

```bash
chroma run --path ./getting-started
```

### Using Docker

```bash
docker pull chromadb/chroma
docker run -p 8000:8000 chromadb/chroma
```

### With Persistent Data

```bash
docker run -v ./chroma-data:/data -p 8000:8000 chromadb/chroma
```

## Client Configuration

### In-Memory Client (Default)

```python
import chromadb
client = chromadb.Client()
```

### HTTP Client

```python
import chromadb
client = chromadb.HttpClient(host='localhost', port=8000)
client.heartbeat()  # Test connection
```

```typescript
import { ChromaClient } from "chromadb";

const client = new ChromaClient({
  host: "localhost",
  port: 8000,
});
await client.heartbeat();
```

## Collections

### Creating Collections

```python
# Create new collection
collection = client.create_collection(name="my_collection")

# Get or create collection (idempotent)
collection = client.get_or_create_collection(name="my_collection")

# Get existing collection
collection = client.get_collection(name="my_collection")
```

### Collection with Metadata

```python
collection = client.create_collection(
    name="my_collection",
    metadata={"description": "My first collection"}
)
```

### Listing Collections

```python
collections = client.list_collections()
for collection in collections:
    print(f"Collection: {collection.name}")
```

### Deleting Collections

```python
client.delete_collection(name="my_collection")
```

## Adding Documents

### Basic Addition

```python
collection.add(
    documents=["This is document 1", "This is document 2"],
    ids=["doc1", "doc2"]
)
```

### With Metadata

```python
collection.add(
    documents=["Document about cats", "Document about dogs"],
    metadatas=[{"category": "animals", "type": "cat"},
               {"category": "animals", "type": "dog"}],
    ids=["doc1", "doc2"]
)
```

### With Custom Embeddings

```python
collection.add(
    documents=["Document 1", "Document 2"],
    embeddings=[[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]],
    ids=["doc1", "doc2"]
)
```

### Upserting (Update or Insert)

```python
# Use upsert for idempotent operations
collection.upsert(
    documents=["Updated document 1", "New document 2"],
    ids=["doc1", "doc2"]
)
```

## Querying

### Basic Query

```python
results = collection.query(
    query_texts=["Find documents about animals"],
    n_results=5
)
```

### Query with Filters

```python
results = collection.query(
    query_texts=["Find cat documents"],
    n_results=3,
    where={"category": "animals", "type": "cat"}
)
```

### Query with Custom Embeddings

```python
results = collection.query(
    query_embeddings=[[0.1, 0.2, 0.3]],
    n_results=5
)
```

### Advanced Filtering

```python
# Multiple conditions
results = collection.query(
    query_texts=["search query"],
    where={
        "$and": [
            {"category": "animals"},
            {"type": {"$ne": "fish"}}  # not equal
        ]
    }
)

# Range queries
results = collection.query(
    query_texts=["search query"],
    where={"score": {"$gt": 0.8}}  # greater than
)

# In operator
results = collection.query(
    query_texts=["search query"],
    where={"type": {"$in": ["cat", "dog"]}}
)
```

## Document Management

### Getting Documents

```python
# Get all documents
documents = collection.get()

# Get specific documents by ID
documents = collection.get(ids=["doc1", "doc2"])

# Get with filters
documents = collection.get(
    where={"category": "animals"},
    limit=10
)
```

### Updating Documents

```python
collection.update(
    ids=["doc1"],
    documents=["Updated document content"],
    metadatas=[{"category": "updated", "version": 2}]
)
```

### Deleting Documents

```python
# Delete by ID
collection.delete(ids=["doc1", "doc2"])

# Delete with filters
collection.delete(where={"category": "temporary"})
```

## Embeddings

### Custom Embedding Functions

```python
from chromadb.utils import embedding_functions

# OpenAI embeddings
openai_ef = embedding_functions.OpenAIEmbeddingFunction(
    api_key="your-api-key",
    model_name="text-embedding-ada-002"
)

collection = client.create_collection(
    name="my_collection",
    embedding_function=openai_ef
)
```

### Sentence Transformers

```python
sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

collection = client.create_collection(
    name="my_collection",
    embedding_function=sentence_transformer_ef
)
```

### Hugging Face Embeddings

```python
huggingface_ef = embedding_functions.HuggingFaceEmbeddingFunction(
    api_key="your-api-key",
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
```

## Authentication

### Basic Authentication

```python
import chromadb
from chromadb.config import Settings

client = chromadb.HttpClient(
    host="localhost",
    port=8000,
    settings=Settings(
        chroma_client_auth_provider="chromadb.auth.basic.BasicAuthClientProvider",
        chroma_client_auth_credentials="admin:admin"
    )
)
```

### Token Authentication

```python
client = chromadb.HttpClient(
    host="localhost",
    port=8000,
    settings=Settings(
        chroma_client_auth_provider="chromadb.auth.token.TokenAuthClientProvider",
        chroma_client_auth_credentials="your-token"
    )
)
```

## Advanced Features

### Distance Metrics

```python
collection = client.create_collection(
    name="my_collection",
    metadata={"hnsw:space": "cosine"}  # cosine, l2, ip
)
```

### Collection Statistics

```python
count = collection.count()
print(f"Collection has {count} documents")
```

### Batch Operations

```python
# Add large batches efficiently
documents = [f"Document {i}" for i in range(1000)]
ids = [f"doc_{i}" for i in range(1000)]

collection.add(
    documents=documents,
    ids=ids
)
```

## Migration

### Installing Migration Tool

```bash
pip install chroma-migrate
chroma-migrate
```

### Legacy Client Migration

```python
# Old way (deprecated)
import chromadb
from chromadb.config import Settings
client = chromadb.Client(Settings(
    chroma_api_impl="rest",
    chroma_server_host="localhost",
    chroma_server_http_port="8000"
))

# New way
import chromadb
client = chromadb.HttpClient(host="localhost", port="8000")
```

## Production Deployment

### Docker Compose

```yaml
version: "3.8"
services:
  chromadb:
    image: chromadb/chroma:latest
    ports:
      - "8000:8000"
    volumes:
      - ./chroma-data:/chroma/chroma
    environment:
      - CHROMA_SERVER_AUTHN_PROVIDER=chromadb.auth.basic_authn.BasicAuthenticationServerProvider
      - CHROMA_SERVER_AUTHN_CREDENTIALS_FILE=/chroma/server.htpasswd
```

### Environment Variables

```bash
export CHROMA_SERVER_HOST=0.0.0.0
export CHROMA_SERVER_HTTP_PORT=8000
export CHROMA_DB_IMPL=clickhouse
export CLICKHOUSE_HOST=localhost
export CLICKHOUSE_PORT=8123
```

## Best Practices

### Performance Optimization

```python
# Use batch operations for large datasets
batch_size = 1000
for i in range(0, len(documents), batch_size):
    batch_docs = documents[i:i+batch_size]
    batch_ids = ids[i:i+batch_size]
    collection.add(documents=batch_docs, ids=batch_ids)
```

### Error Handling

```python
try:
    collection = client.create_collection(name="my_collection")
except Exception as e:
    print(f"Collection creation failed: {e}")
    collection = client.get_collection(name="my_collection")
```

### Memory Management

```python
# Use get_or_create_collection for idempotent operations
collection = client.get_or_create_collection(name="my_collection")

# Use upsert instead of add for repeated runs
collection.upsert(
    documents=documents,
    ids=ids
)
```

## Common Use Cases

### RAG (Retrieval-Augmented Generation)

```python
def rag_query(question, collection, llm_client):
    # Retrieve relevant documents
    results = collection.query(
        query_texts=[question],
        n_results=5
    )

    # Combine documents as context
    context = "\n".join(results['documents'][0])

    # Generate response with LLM
    prompt = f"Context: {context}\n\nQuestion: {question}\nAnswer:"
    response = llm_client.generate(prompt)

    return response
```

### Semantic Search

```python
def semantic_search(query, collection, threshold=0.7):
    results = collection.query(
        query_texts=[query],
        n_results=10
    )

    # Filter by similarity threshold
    filtered_results = []
    for i, distance in enumerate(results['distances'][0]):
        if distance < threshold:  # Lower distance = higher similarity
            filtered_results.append({
                'document': results['documents'][0][i],
                'metadata': results['metadatas'][0][i],
                'similarity': 1 - distance
            })

    return filtered_results
```

### Document Clustering

```python
def find_similar_documents(doc_id, collection, n_similar=5):
    # Get the document
    doc = collection.get(ids=[doc_id])

    if not doc['documents']:
        return []

    # Find similar documents
    results = collection.query(
        query_texts=doc['documents'],
        n_results=n_similar + 1  # +1 to exclude the original
    )

    # Remove the original document from results
    similar_docs = []
    for i, result_id in enumerate(results['ids'][0]):
        if result_id != doc_id:
            similar_docs.append({
                'id': result_id,
                'document': results['documents'][0][i],
                'similarity': 1 - results['distances'][0][i]
            })

    return similar_docs[:n_similar]
```

This documentation covers the essential features of ChromaDB for building applications with vector embeddings and semantic search capabilities.
