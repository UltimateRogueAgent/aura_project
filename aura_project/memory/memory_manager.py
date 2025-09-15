from typing import Any, Dict, List
from .vector_store import VectorStoreManager

class MemoryManager:
    """
    Manages the application's memory, including context management,
    compression, and cleanup.
    """

    def __init__(self, vector_store: VectorStoreManager, config: Dict[str, Any]):
        """
        Initializes the MemoryManager.

        Args:
            vector_store: An instance of VectorStoreManager.
            config: A dictionary containing configuration for memory management.
        """
        self.vector_store = vector_store
        self.config = config
        self.context_window = config.get("context_window", 8000)
        self.conversation_history: List[str] = []

    def manage_context(self) -> List[str]:
        """
        Manages the context of a conversation to stay within the context window.
        A more advanced implementation would use token counting.
        """
        current_context_size = self.get_context_size()
        while current_context_size > self.context_window and self.conversation_history:
            self.conversation_history.pop(0)
            current_context_size = self.get_context_size()

        return self.conversation_history

    def add_to_history(self, message: str):
        """
        Adds a message to the conversation history and manages the context size.
        """
        self.conversation_history.append(message)
        self.manage_context()

    def get_context_size(self) -> int:
        """
        Calculates the total number of characters in the conversation history.
        """
        return sum(len(message) for message in self.conversation_history)

    def compress_context(self) -> str:
        """
        Compresses the current conversation history into a summary.
        This is a placeholder for a more sophisticated summarization mechanism.
        """
        print("Compressing context...")
        # In a real implementation, this would use an LLM.
        return " ".join(self.conversation_history)

    def cleanup_memory(self, max_memories: int) -> int:
        """
        Cleans up old or irrelevant memories from the vector store.
        """
        current_count = self.vector_store.get_statistics().get("memory_count", 0)
        deleted_count = 0
        if current_count > max_memories:
            num_to_delete = current_count - max_memories
            # This is a naive implementation. A better approach would be to
            # retrieve memories with their timestamps and delete the oldest.
            # ChromaDB's API would need to support this efficiently.
            print(f"Memory limit exceeded. Placeholder for deleting {num_to_delete} memories.")
            pass
        return deleted_count

    def get_statistics(self) -> Dict[str, Any]:
        """
        Gets statistics about the memory and context.
        """
        return {
            "vector_store_stats": self.vector_store.get_statistics(),
            "context_window": self.context_window,
            "current_context_size_chars": self.get_context_size(),
            "conversation_history_length": len(self.conversation_history),
        }
