from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application configuration loaded from environment variables."""

    app_name: str = "Production RAG Platform"
    app_env: str = "development"
    log_level: str = "INFO"

    llm_provider: str = "ollama"
    embedding_provider: str = "local"

    ollama_base_url: str = "http://localhost:11434"
    ollama_model: str = "llama3.2"

    openai_api_key: str | None = None
    openai_embedding_model: str = "text-embedding-3-small"

    vector_store: str = "faiss"
    data_dir: Path = Path("data")
    index_dir: Path = Path("data/indexes")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    """Return a cached application settings instance."""
    return Settings()