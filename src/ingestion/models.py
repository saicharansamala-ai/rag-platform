from datetime import datetime, timezone
from typing import Any

from pydantic import BaseModel, Field


class Document(BaseModel):
    """Normalized document representation used throughout the RAG pipeline."""

    content: str
    source: str

    document_type: str

    metadata: dict[str, Any] = Field(default_factory=dict)

    page: int | None = None
    timestamp_start: float | None = None
    timestamp_end: float | None = None

    content_hash: str

    ingested_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )