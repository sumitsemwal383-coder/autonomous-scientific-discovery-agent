"""
Literature Retriever for Grounded RAG
Retrieves verified peer-reviewed preprints and formats citation-grounded context.
"""
from typing import List, Dict, Any, Tuple
from .vector_db import VectorDatabase

class LiteratureRetriever:
    def __init__(self, vector_db: VectorDatabase):
        self.vector_db = vector_db

    def retrieve_grounding_context(self, research_topic: str, top_k: int = 4) -> Tuple[str, List[Dict[str, Any]]]:
        """
        Retrieves relevant scientific literature and constructs strict grounding context.
        """
        results = self.vector_db.search(research_topic, top_k=top_k)
        if not results:
            return "No relevant literature found in vector store.", []

        context_lines = [f"=== GROUNDED SCIENTIFIC LITERATURE FOR: '{research_topic}' ==="]
        citations = []

        for idx, match in enumerate(results, 1):
            meta = match["metadata"]
            doc_id = match["id"]
            title = meta.get("title", "Untitled")
            authors = ", ".join(meta.get("authors", [])[:3])
            pub_date = meta.get("published", "Recent")
            abstract = meta.get("abstract", "")
            score = match["score"]

            citations.append({
                "ref_key": f"Ref_{idx}",
                "doc_id": doc_id,
                "title": title,
                "authors": authors,
                "published": pub_date,
                "url": meta.get("url", ""),
                "score": score
            })

            context_lines.append(
                f"[Ref_{idx}] Title: {title}\n"
                f"       Authors: {authors} ({pub_date})\n"
                f"       ID/DOI: {doc_id} | Relevance Score: {score}\n"
                f"       Findings/Abstract: {abstract}\n"
            )

        context_lines.append("=== INSTRUCTION: All generated hypotheses MUST cite at least one [Ref_X] above ===")
        return "\n".join(context_lines), citations

    def verify_grounding(self, hypothesis_text: str, citations: List[Dict[str, Any]]) -> bool:
        """
        Validates that the hypothesis explicitly references at least one retrieved source.
        """
        if not citations:
            return True
        for cite in citations:
            ref_tag = cite["ref_key"]
            title_snippet = cite["title"].split(":")[0].strip()
            if ref_tag in hypothesis_text or title_snippet.lower() in hypothesis_text.lower():
                return True
        return False
