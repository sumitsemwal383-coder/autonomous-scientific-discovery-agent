"""
Ingestion Pipeline Tests
Validates querying and parsing logic for ArXiv and PubMed preprints.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.ingestion.arxiv_pipeline import ArxivPipeline
from src.ingestion.pubmed_pipeline import PubMedPipeline

def test_arxiv_ingestion():
    pipeline = ArxivPipeline()
    papers = pipeline.search("reinforcement learning", max_results=2)
    assert len(papers) >= 2
    for p in papers:
        assert p["source"] == "arxiv"
        assert len(p["title"]) > 0
        assert len(p["abstract"]) > 0

def test_pubmed_ingestion():
    pipeline = PubMedPipeline()
    papers = pipeline.search("artificial intelligence discovery", max_results=2)
    assert len(papers) >= 2
    for p in papers:
        assert p["source"] == "pubmed"
        assert len(p["title"]) > 0

if __name__ == "__main__":
    test_arxiv_ingestion()
    test_pubmed_ingestion()
    print("[SUCCESS] All Ingestion pipeline tests passed successfully!")
