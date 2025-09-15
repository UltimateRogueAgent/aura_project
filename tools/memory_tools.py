from typing import Dict, Any
from ..memory.vector_memory import VectorMemory

def memory_search_tool(query: str, vector_memory: VectorMemory, k: int = 5) -> str:
    """
    A tool for searching for memories in the vector store.

    Args:
        query: The query to search for.
        vector_memory: An instance of the VectorMemory class.
        k: The number of results to return.

    Returns:
        A string representation of the search results.
    """
    if not isinstance(vector_memory, VectorMemory):
        return "Error: A valid VectorMemory instance must be provided."

    results = vector_memory.search_memory(query, k)
    return str(results)

def memory_save_tool(text: str, vector_memory: VectorMemory, metadata: Dict = None) -> str:
    """
    A tool for saving a piece of text as a memory in the vector store.

    Args:
        text: The text content to save as a memory.
        vector_memory: An instance of the VectorMemory class.
        metadata: Optional metadata to store with the memory.

    Returns:
        A confirmation message with the ID of the saved memory.
    """
    if not isinstance(vector_memory, VectorMemory):
        return "Error: A valid VectorMemory instance must be provided."

    memory_id = vector_memory.save_memory(text, metadata)
    return f"Memory saved successfully with ID: {memory_id}"
