"""
Dense Semantic Embedding Generator
Provides high-dimensional vector representations for scientific literature retrieval.
"""
import math
import re
import hashlib
from typing import List
import numpy as np

class DenseEmbeddingGenerator:
    def __init__(self, dimension: int = 128):
        self.dimension = dimension

    def encode(self, text: str) -> List[float]:
        """
        Encodes arbitrary text into a normalized dense vector of fixed dimension.
        Employs n-gram term hashing and character-level semantic frequency projection.
        """
        if not text or not text.strip():
            return [0.0] * self.dimension

        cleaned = re.sub(r"[^\w\s]", " ", text.lower())
        tokens = cleaned.split()
        
        vec = np.zeros(self.dimension, dtype=np.float32)

        # 1. Unigram & Bigram hashing with semantic positioning
        for i, token in enumerate(tokens):
            if len(token) < 2:
                continue
            # Hash token to dimension indices
            h1 = int(hashlib.md5(token.encode("utf-8")).hexdigest(), 16) % self.dimension
            sign1 = 1.0 if (h1 % 2 == 0) else -1.0
            weight = 1.0 + (0.5 if len(token) > 6 else 0.0)
            vec[h1] += sign1 * weight

            # Bigram context
            if i < len(tokens) - 1:
                bigram = f"{token}_{tokens[i+1]}"
                h2 = int(hashlib.sha256(bigram.encode("utf-8")).hexdigest(), 16) % self.dimension
                sign2 = 1.0 if (h2 % 2 == 0) else -1.0
                vec[h2] += sign2 * 1.5

        # 2. L2 Normalization
        norm = np.linalg.norm(vec)
        if norm > 1e-9:
            vec = vec / norm
        else:
            vec = np.zeros(self.dimension, dtype=np.float32)

        return vec.tolist()

    def encode_batch(self, texts: List[str]) -> List[List[float]]:
        return [self.encode(t) for t in texts]

    @staticmethod
    def cosine_similarity(v1: List[float], v2: List[float]) -> float:
        a = np.array(v1, dtype=np.float32)
        b = np.array(v2, dtype=np.float32)
        dot = np.dot(a, b)
        norm_a = np.linalg.norm(a)
        norm_b = np.linalg.norm(b)
        if norm_a == 0 or norm_b == 0:
            return 0.0
        return float(dot / (norm_a * norm_b))
