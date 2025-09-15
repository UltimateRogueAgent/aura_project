import ollama
from typing import Any, Dict, List

class OllamaClient:
    """
    A client for interacting with the Ollama LLM server.
    """

    def __init__(self, config: Dict[str, Any]):
        """
        Initializes the Ollama client.

        Args:
            config: A dictionary containing configuration for the client,
                    such as host and port.
        """
        self.host = config.get("host", "http://localhost")
        self.port = config.get("port", 11434)
        self.client = ollama.AsyncClient(host=f"{self.host}:{self.port}")
        self.cache: Dict[str, str] = {}

    async def check_connection(self) -> bool:
        """
        Checks the connection to the Ollama server.

        Returns:
            True if the connection is successful, False otherwise.
        """
        try:
            await self.client.list()
            return True
        except Exception as e:
            print(f"Failed to connect to Ollama server: {e}")
            return False

    async def list_models(self) -> List[str]:
        """
        Lists the available models on the Ollama server.

        Returns:
            A list of model names.
        """
        try:
            models_info = await self.client.list()
            return [model['name'] for model in models_info['models']]
        except Exception as e:
            print(f"Failed to list models: {e}")
            return []

    async def generate(self, model: str, prompt: str) -> str:
        """
        Generates a response from a model.

        Args:
            model: The name of the model to use.
            prompt: The prompt to send to the model.

        Returns:
            The generated response.
        """
        cache_key = f"{model}:{prompt}"
        if cache_key in self.cache:
            return self.cache[cache_key]

        try:
            response = await self.client.generate(model=model, prompt=prompt)
            result = response['response']
            self.cache[cache_key] = result
            return result
        except Exception as e:
            print(f"Failed to generate response: {e}")
            return ""

    async def get_model_info(self, model: str) -> Dict[str, Any]:
        """
        Gets information about a specific model.

        Args:
            model: The name of the model.

        Returns:
            A dictionary containing model information.
        """
        try:
            return await self.client.show(model_name=model)
        except Exception as e:
            print(f"Failed to get model info: {e}")
            return {}
