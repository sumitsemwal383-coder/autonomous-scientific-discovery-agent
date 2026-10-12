"""
Unit Tests for Statistical Critic Agent
Verifies evaluation of p-values, 95% confidence intervals, Cohen's d effect sizes, and power.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.agents.critic_agent import CriticAgent

def test_critic_confirms_statistically_significant_result():
    critic = CriticAgent(alpha=0.05)
    sample_metrics = {
        "baseline_mean": 70.0,
        "baseline_std": 6.5,
        "treatment_mean": 82.5,
        "treatment_std": 5.2,
        "mean_difference": 12.5,
        "t_statistic": 4.82,
        "p_value": 0.00003,
        "cohens_d": 0.95,
        "ci_95_low": 7.4,
        "ci_95_high": 17.6,
        "sample_size": 100
    }
    res = critic.execute({"metrics": sample_metrics, "hypothesis": {}})
    assert res["verdict"] == "CONFIRMED_STATISTICALLY_SIGNIFICANT"
    assert res["is_significant"] is True
    assert res["effect_magnitude"] == "Large Effect"
    assert res["estimated_power"] >= 0.80

def test_critic_rejects_insignificant_result():
    critic = CriticAgent(alpha=0.05)
    sample_metrics = {
        "baseline_mean": 70.0,
        "baseline_std": 6.5,
        "treatment_mean": 71.0,
        "treatment_std": 6.8,
        "mean_difference": 1.0,
        "t_statistic": 0.85,
        "p_value": 0.395,
        "cohens_d": 0.12,
        "ci_95_low": -1.2,
        "ci_95_high": 3.2,
        "sample_size": 100
    }
    res = critic.execute({"metrics": sample_metrics, "hypothesis": {}})
    assert res["verdict"] == "REJECTED_INSIGNIFICANT"
    assert res["is_significant"] is False
    assert res["effect_magnitude"] == "Negligible Effect"

if __name__ == "__main__":
    test_critic_confirms_statistically_significant_result()
    test_critic_rejects_insignificant_result()
    print("[SUCCESS] All Statistical Critic Agent tests passed successfully!")
