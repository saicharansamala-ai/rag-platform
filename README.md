# Production RAG Platform

A production-oriented Retrieval-Augmented Generation platform built with Python.

## Goals

- Multi-format document ingestion
- Production-grade chunking strategies
- Multiple embedding providers
- Multiple vector stores
- Dense, lexical and hybrid retrieval
- Cross-encoder reranking
- Grounded generation with citations
- RAG evaluation and regression testing
- FastAPI backend
- CLI
- Streamlit UI
- Docker deployment
- CI/CD
- Observability
- Security and guardrails

## Architecture

```text
Documents
   ↓
Ingestion
   ↓
Chunking
   ↓
Embeddings
   ↓
Vector Store
   ↓
Retrieval
   ↓
Reranking
   ↓
Generation
   ↓
Evaluation
   ↓
FastAPI / CLI / Streamlit