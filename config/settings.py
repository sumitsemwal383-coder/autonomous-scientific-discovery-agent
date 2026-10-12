"""
Configuration and Settings for Autonomous Multimodal Scientific Discovery Agent.
Enterprise Grade - Zaalima Development Compliant
"""
import os
from pathlib import Path

# Base Paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
CACHE_DIR = DATA_DIR / "cache"
VECTOR_STORE_DIR = DATA_DIR / "vector_store"
HOLDOUT_DIR = DATA_DIR / "holdout_papers"
SYNTHESIS_DIR = PROJECT_ROOT / "data" / "synthesis"
TEMPLATES_DIR = PROJECT_ROOT / "src" / "synthesis" / "templates"
DOCKER_DIR = PROJECT_ROOT / "docker"

# Create directories if not existing
for directory in [DATA_DIR, CACHE_DIR, VECTOR_STORE_DIR, HOLDOUT_DIR, SYNTHESIS_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

# ArXiv & PubMed API Configuration
ARXIV_API_URL = "http://export.arxiv.org/api/query"
PUBMED_ESEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
PUBMED_ESUMMARY_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
PUBMED_EFETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

# Sandboxed Code Execution Policy
SANDBOX_TIMEOUT_SECONDS = 30
SANDBOX_MAX_MEMORY_MB = 512
SANDBOX_ENABLE_DOCKER = os.getenv("ENABLE_DOCKER_SANDBOX", "false").lower() == "true"
SANDBOX_DISALLOWED_IMPORTS = [
    "os.system",
    "subprocess",
    "shutil.rmtree",
    "ctypes",
    "socket",
    "requests",
    "urllib",
    "http",
    "ftplib",
    "telnetlib",
    "paramiko",
    "pty",
    "fcntl",
    "pwd",
    "grp",
    "sys.exit",
    "exit",
    "quit",
    "builtins.__import__",
]

# Statistical Critic Configuration
STATISTICAL_ALPHA_DEFAULT = 0.05
STATISTICAL_CONFIDENCE_INTERVAL = 0.95
MIN_STATISTICAL_POWER = 0.80
EFFECT_SIZE_MODERATE_THRESHOLD = 0.50

# LLM & Model Execution Settings
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "mock_heuristic")  # options: "mock_heuristic", "openai", "gemini"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

# Context Window & Memory Limits
MAX_CONTEXT_TOKENS = 8192
SLIDING_WINDOW_HISTORY = 10
MEMORY_SUMMARY_THRESHOLD_TOKENS = 4096

# RL Feedback Loop
RL_MAX_DEBUG_ITERATIONS = 4
RL_REWARD_SYNTAX_PASS = 0.25
RL_REWARD_EXEC_PASS = 0.25
RL_REWARD_STAT_PASS = 0.35
RL_REWARD_NOVELTY_PASS = 0.15
