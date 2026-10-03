from pathlib import Path

from .hashing import sha256_file
from .models import Document


def load_text(path: Path) -> Document:
    """Load a UTF-8 text file into the normalized Document model."""

    content = path.read_text(encoding="utf-8")

    return Document(
        content=content,
        source=str(path),
        document_type="text",
        content_hash=sha256_file(path),
        metadata={
            "filename": path.name,
            "extension": path.suffix.lower(),
        },
    )