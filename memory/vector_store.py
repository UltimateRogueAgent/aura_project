import chromadb
from typing import Any, Dict, List
from dataclasses import dataclass
from datetime import datetime
import uuid

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

class VectorStoreManager:
    """
    Manages the vector store for AURA's memory.
    """

    def __init__(self, config: Dict[str, Any], embedding_function: Any = None):
        """
        Initializes the VectorStoreManager.

        Args:
            config: A dictionary containing configuration for the vector store.
            embedding_function: The function to use for creating embeddings.
        """
        self.path = config.get("path", "./data/chroma_db")
        self.collection_name = config.get("collection_name", "aura_memory")
        self.client = chromadb.PersistentClient(path=self.path)
        self.collection = self.client.get_or_create_collection(
            name=self.collection_name,
            embedding_function=embedding_function
        )

    def add_memory(self, text: str, metadata: Dict = None) -> str:
        """
        Adds a memory to the vector store.

        Args:
            text: The text content of the memory.
            metadata: A dictionary of metadata for the memory.

        Returns:
            The ID of the added memory.
        """
        memory_id = str(uuid.uuid4())
        if metadata is None:
            metadata = {}

        metadata["timestamp"] = datetime.now().isoformat()

        self.collection.add(
            documents=[text],
            metadatas=[metadata],
            ids=[memory_id]
        )
        return memory_id

    def search_memory(self, query: str, k: int = 5) -> List[Dict]:
        """
        Searches for memories in the vector store.

        Args:
            query: The query to search for.
            k: The number of results to return.

        Returns:
            A list of search results.
        """
        results = self.collection.query(
            query_texts=[query],
            n_results=k
        )
        return results

    def delete_memory(self, memory_id: str) -> bool:
        """
        Deletes a memory from the vector store.

        Args:
            memory_id: The ID of the memory to delete.

        Returns:
            True if the memory was deleted successfully, False otherwise.
        """
        try:
            self.collection.delete(ids=[memory_id])
            return True
        except Exception as e:
            print(f"Error deleting memory {memory_id}: {e}")
            return False

    def get_statistics(self) -> Dict[str, Any]:
        """
        Gets statistics about the vector store.

        Returns:
            A dictionary of statistics.
        """
        return {
            "collection_name": self.collection_name,
            "path": self.path,
            "memory_count": self.collection.count()
        }
