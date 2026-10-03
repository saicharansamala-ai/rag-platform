from pathlib import Path

from ingestion.text import load_text


def test_load_text() -> None:
    path = Path("data/raw/sample.txt")

    document = load_text(path)

    assert document.document_type == "text"
    assert document.source == str(path)
    assert document.content
    assert len(document.content_hash) == 64
    assert document.metadata["filename"] == "sample.txt"