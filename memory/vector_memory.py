from typing import Any, Dict, List
from langchain_community.embeddings import OllamaEmbeddings
from .vector_store import VectorStoreManager

class VectorMemory:
    """
    A class for managing memories in a vector store, using Ollama for embeddings.
    This class serves as a higher-level abstraction over the VectorStoreManager.
    """

    def __init__(self, config: Dict[str, Any]):
        """
        Initializes the VectorMemory system.

        Args:
            config: A dictionary containing configuration for the memory system,
                    including the Ollama model and vector store settings.
        """
        ollama_model = config.get("ollama_model", "rogue-v1-agent")
        self.embedding_function = OllamaEmbeddings(model=ollama_model)

        vector_store_config = config.get("vector_store", {})
        self.vector_store = VectorStoreManager(
            config=vector_store_config,
            embedding_function=self.embedding_function
        )

    def save_memory(self, text: str, metadata: Dict = None) -> str:
        """
        Saves a memory (a piece of text) to the vector store.
        """
        return self.vector_store.add_memory(text, metadata)

    def search_memory(self, query: str, k: int = 5) -> List[Dict]:
        """
        Searches for memories in the vector store that are similar to the query.
        """
        return self.vector_store.search_memory(query, k)

    def get_statistics(self) -> Dict[str, Any]:
        """
        Gets statistics about the underlying vector store.
        """
        return self.vector_store.get_statistics()
