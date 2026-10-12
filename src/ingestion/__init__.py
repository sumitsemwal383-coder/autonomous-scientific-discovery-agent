"""Data Ingestion Module for Autonomous Scientific Discovery Agent."""
from .arxiv_pipeline import ArxivPipeline
from .pubmed_pipeline import PubMedPipeline
from .multimodal_parser import MultimodalParser

__all__ = ["ArxivPipeline", "PubMedPipeline", "MultimodalParser"]
