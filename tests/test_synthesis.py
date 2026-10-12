"""
LaTeX Synthesis Tests
Validates that generated papers contain all required academic sections, metrics, and BibTeX entries.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.synthesis.latex_generator import LatexPaperGenerator

def test_latex_generation():
    generator = LatexPaperGenerator()
    hypo_data = {
        "hypothesis": {
            "title": "Automated Multi-Agent Empirical Discovery",
            "statement": "Statistical regularization enhances convergence of autonomous scientific reasoning agents.",
            "formal_hypotheses": {"H0": "No effect (p >= 0.05)", "H1": "Significant gain (p < 0.05)"},
            "variables": {"independent": "Critic Agent", "dependent": "Accuracy", "controlled": "Seed"},
            "grounding_citations": [
                {"authors": "Zelikman et al.", "title": "Quiet-STaR", "published": "2024", "url": "https://arxiv.org/abs/2403.09629"}
            ]
        }
    }
    exp_data = {
        "metrics": {
            "sample_size": 100,
            "baseline_mean": 71.2,
            "baseline_std": 6.8,
            "treatment_mean": 83.4,
            "treatment_std": 5.1,
            "mean_difference": 12.2,
            "t_statistic": 5.41,
            "p_value": 0.00001,
            "cohens_d": 0.98,
            "ci_95_low": 7.8,
            "ci_95_high": 16.6
        }
    }
    critic_data = {
        "verdict": "CONFIRMED_STATISTICALLY_SIGNIFICANT",
        "effect_magnitude": "Large Effect",
        "critique": "Observed p-value < 0.05 and 95% CI excludes zero."
    }
    lit_data = {"literature_synthesis": "Survey of current agents."}

    res = generator.compile_research_paper(hypo_data, exp_data, critic_data, lit_data)
    assert res["status"] == "SUCCESS"
    assert Path(res["tex_path"]).exists()
    assert Path(res["bib_path"]).exists()
    assert "\\begin{document}" in res["rendered_tex"]
    assert "Cohen's $d$ Effect Size" in res["rendered_tex"]

if __name__ == "__main__":
    test_latex_generation()
    print("[SUCCESS] All LaTeX Paper Synthesis tests passed successfully!")
