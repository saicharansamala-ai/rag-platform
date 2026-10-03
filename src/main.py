from utils.config import get_settings
from utils.logging_config import configure_logging, get_logger

logger = get_logger(__name__)


def main() -> None:
    """Run the application startup check."""

    settings = get_settings()
    configure_logging(settings.log_level)

    logger.info("Starting %s", settings.app_name)
    logger.info("Environment: %s", settings.app_env)
    logger.info("LLM provider: %s", settings.llm_provider)
    logger.info("Embedding provider: %s", settings.embedding_provider)
    logger.info("Vector store: %s", settings.vector_store)


if __name__ == "__main__":
    main()