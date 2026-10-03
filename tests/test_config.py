from utils.config import get_settings


def test_settings_defaults() -> None:
    settings = get_settings()

    assert settings.app_name == "Production RAG Platform"
    assert settings.llm_provider in {"ollama", "openai"}
    assert settings.embedding_provider in {"local", "openai"}