"""
Hierarchical Context Window Memory Manager
Maintains agent coherence, manages token budget, compresses multi-day experimental history,
and prevents context degradation over long-running scientific discovery workflows.
"""
import logging
from typing import List, Dict, Any, Optional
from config.settings import MAX_CONTEXT_TOKENS, SLIDING_WINDOW_HISTORY, MEMORY_SUMMARY_THRESHOLD_TOKENS

logger = logging.getLogger(__name__)

class ContextMemoryManager:
    def __init__(
        self,
        max_tokens: int = MAX_CONTEXT_TOKENS,
        sliding_window_size: int = SLIDING_WINDOW_HISTORY,
        summary_threshold: int = MEMORY_SUMMARY_THRESHOLD_TOKENS
    ):
        self.max_tokens = max_tokens
        self.sliding_window_size = sliding_window_size
        self.summary_threshold = summary_threshold
        
        # Memory stores
        self.working_memory: Dict[str, Any] = {}
        self.episodic_history: List[Dict[str, Any]] = []
        self.compressed_summaries: List[str] = []
        self.total_tokens_consumed = 0

    def estimate_tokens(self, text: str) -> int:
        """Heuristic token estimation (~4 characters per token)."""
        return max(1, len(text) // 4)

    def add_interaction(self, agent_role: str, action: str, content: str, metadata: Optional[Dict[str, Any]] = None) -> None:
        """
        Records a new agent event and performs automated compaction if token threshold is exceeded.
        """
        token_cost = self.estimate_tokens(content)
        self.total_tokens_consumed += token_cost

        entry = {
            "role": agent_role,
            "action": action,
            "content": content,
            "tokens": token_cost,
            "metadata": metadata or {}
        }
        self.episodic_history.append(entry)

        # Trigger automatic consolidation if context is nearing boundary
        current_active_tokens = sum(e["tokens"] for e in self.episodic_history)
        if current_active_tokens > self.summary_threshold:
            self._compress_oldest_episodes()

    def get_consolidated_context(self) -> str:
        """
        Assembles coherent prompt context combining compressed summaries + recent sliding window.
        """
        context_parts = []

        # 1. High-level multi-day summaries
        if self.compressed_summaries:
            context_parts.append("=== COMPRESSED HISTORICAL SUMMARY ===")
            for s in self.compressed_summaries:
                context_parts.append(f"• {s}")
            context_parts.append("")

        # 2. Recent high-fidelity episodic events
        context_parts.append("=== ACTIVE EXPERIMENTAL CONTEXT ===")
        recent = self.episodic_history[-self.sliding_window_size:]
        for entry in recent:
            context_parts.append(f"[{entry['role']} - {entry['action']}]: {entry['content'][:500]}")

        return "\n".join(context_parts)

    def _compress_oldest_episodes(self) -> None:
        """Compresses aging episodic items into a concise milestone representation."""
        if len(self.episodic_history) <= self.sliding_window_size:
            return

        to_compress = self.episodic_history[:-self.sliding_window_size]
        roles_involved = set(e["role"] for e in to_compress)
        summary_text = (
            f"Archived {len(to_compress)} experimental actions involving {', '.join(roles_involved)}. "
            f"Key activities: {to_compress[0]['action']} through {to_compress[-1]['action']}."
        )
        self.compressed_summaries.append(summary_text)
        self.episodic_history = self.episodic_history[-self.sliding_window_size:]
        logger.info(f"Context memory compacted: {summary_text}")

    def get_token_metrics(self) -> Dict[str, Any]:
        current_tokens = sum(e["tokens"] for e in self.episodic_history)
        return {
            "total_tokens_consumed": self.total_tokens_consumed,
            "active_context_tokens": current_tokens,
            "max_context_tokens": self.max_tokens,
            "utilization_pct": round((current_tokens / self.max_tokens) * 100, 2),
            "episodes_retained": len(self.episodic_history),
            "compressed_milestones": len(self.compressed_summaries)
        }
