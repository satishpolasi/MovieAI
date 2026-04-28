import os
import sys
import json
from dotenv import load_dotenv
from utils.config_loader import load_config
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from logger import GLOBAL_LOGGER as log
from exception.custom_exception import MovieAIException
import asyncio

load_dotenv()  # Load environment variables from .env file

class ApiKeyManager:
    def __init__(self):
        self.api_keys = {
            "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY"),
            "GOOGLE_API_KEY": os.getenv("GOOGLE_API_KEY"),
            "ANTHROPIC_API_KEY": os.getenv("ANTHROPIC_API_KEY"),
        }

        # Just log loaded keys (don't print actual values)
        for key, val in self.api_keys.items():
            if val:
                log.info(f"{key} loaded from environment")
            else:
                log.warning(f"{key} is missing from environment")

    def get(self, key: str):
        return self.api_keys.get(key)


    def get(self, key: str) -> str:
        val = self.api_keys.get(key)
        if not val:
            raise KeyError(f"API key for {key} is missing")
        return val

class ModelLoader:
    """
    Loads LLMs based on config and environment.
    """

    def __init__(self):
        self.api_key_mgr = ApiKeyManager()
        self.config = load_config()
        log.info("YAML config loaded", config_keys=list(self.config.keys()))


    def load_llm(self):
        """
        Load and return the configured LLM model.
        """
        llm_block = self.config["llm"]
        provider_key = os.getenv("LLM_PROVIDER", "anthropic")

        if provider_key not in llm_block:
            log.error("LLM provider not found in config", provider=provider_key)
            raise ValueError(f"LLM provider '{provider_key}' not found in config")

        llm_config = llm_block[provider_key]
        provider = llm_config.get("provider")
        model_name = llm_config.get("model_name")
        temperature = llm_config.get("temperature", 0.5)
        max_tokens = llm_config.get("max_output_tokens", 2000)

        log.info("Loading LLM", provider=provider, model=model_name)

        if provider == "google":
            return ChatGoogleGenerativeAI(
                model=model_name,
                google_api_key=self.api_key_mgr.get("GOOGLE_API_KEY"),
                temperature=temperature,
                max_output_tokens=max_tokens
            )
        
        elif provider == "anthropic":
            return ChatAnthropic(
                model=model_name,
                api_key=self.api_key_mgr.get("ANTHROPIC_API_KEY"),
                temperature=temperature,
                max_tokens=max_tokens
            )
        
        elif provider == "openai":
            return ChatOpenAI(
                model=model_name,
                api_key=self.api_key_mgr.get("OPENAI_API_KEY"),
                temperature=temperature,
                max_tokens=max_tokens
            )
        
        else:
            log.error("Unsupported LLM provider", provider=provider)
            raise ValueError(f"Unsupported LLM provider: {provider}")


if __name__ == "__main__":
    loader = ModelLoader()

    # Test LLM
    llm = loader.load_llm()
    print(f"LLM Loaded: {llm}")
    result = llm.invoke("Hello, how are you?")
    print(f"LLM Result: {result.content}")