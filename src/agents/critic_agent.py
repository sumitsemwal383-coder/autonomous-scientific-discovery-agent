"""
Statistical Critic Agent
Rigorously evaluates the empirical output of the Code Executor agent, assessing statistical
significance, computing p-values, 95% confidence intervals, Cohen's d effect sizes, and statistical power.
"""
from typing import Dict, Any
from .base_agent import BaseAgent
from config.settings import (
    STATISTICAL_ALPHA_DEFAULT,
    STATISTICAL_CONFIDENCE_INTERVAL,
    MIN_STATISTICAL_POWER,
    EFFECT_SIZE_MODERATE_THRESHOLD
)

class CriticAgent(BaseAgent):
    def __init__(self, alpha: float = STATISTICAL_ALPHA_DEFAULT):
        super().__init__(
            name="Empirical Statistical Critic",
            role="Statistical Critic Agent",
            description="Evaluates p-values, confidence intervals, effect sizes, and statistical power to confirm or refute hypotheses."
        )
        self.alpha = alpha

    def execute(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        metrics = inputs.get("metrics", {})
        hypothesis = inputs.get("hypothesis", {})

        p_val = metrics.get("p_value", 1.0)
        cohen_d = metrics.get("cohens_d", 0.0)
        ci_low = metrics.get("ci_95_low", 0.0)
        ci_high = metrics.get("ci_95_high", 0.0)
        sample_size = metrics.get("sample_size", 0)
        mean_diff = metrics.get("mean_difference", 0.0)

        self.log_action("AUDIT_STATISTICS", f"Auditing empirical metrics: p={p_val:.5e}, d={cohen_d:.2f}, CI=[{ci_low:.2f}, {ci_high:.2f}]")

        # 1. Evaluate P-Value against significance threshold alpha
        p_significant = p_val < self.alpha

        # 2. Evaluate Confidence Interval: does CI cross zero?
        ci_excludes_zero = not (ci_low <= 0 <= ci_high)

        # 3. Categorize Effect Size (Cohen's d convention)
        if abs(cohen_d) >= 0.8:
            effect_magnitude = "Large Effect"
        elif abs(cohen_d) >= EFFECT_SIZE_MODERATE_THRESHOLD:
            effect_magnitude = "Moderate Effect"
        elif abs(cohen_d) >= 0.2:
            effect_magnitude = "Small Effect"
        else:
            effect_magnitude = "Negligible Effect"

        # 4. Statistical Power estimation (heuristic based on sample size and d)
        estimated_power = min(1.0, 0.5 + (sample_size / 200.0) * (abs(cohen_d) / 0.8))
        power_adequate = estimated_power >= MIN_STATISTICAL_POWER

        # 5. Formulate Rigorous Statistical Verdict
        if p_significant and ci_excludes_zero and abs(cohen_d) >= 0.3 and power_adequate:
            verdict = "CONFIRMED_STATISTICALLY_SIGNIFICANT"
            critique = (
                f"Empirical validation rejects the null hypothesis H0 at alpha={self.alpha}. "
                f"The observed mean difference of {mean_diff:.2f} is statistically significant "
                f"(t={metrics.get('t_statistic', 0):.2f}, p={p_val:.4e}). "
                f"Cohen's d of {cohen_d:.2f} confirms a {effect_magnitude}. "
                f"The 95% Confidence Interval [{ci_low:.2f}, {ci_high:.2f}] strictly excludes zero. "
                f"Estimated statistical power ({estimated_power:.2f}) satisfies standard beta threshold (0.80)."
            )
        elif p_significant and not power_adequate:
            verdict = "INCONCLUSIVE_UNDERPOWERED"
            critique = f"Observed p < {self.alpha}, but sample size N={sample_size} yields insufficient power ({estimated_power:.2f})."
        else:
            verdict = "REJECTED_INSIGNIFICANT"
            critique = (
                f"Fail to reject the null hypothesis H0. P-value ({p_val:.4f}) >= {self.alpha} or "
                f"the 95% CI [{ci_low:.2f}, {ci_high:.2f}] crosses zero. Observed effect is statistically indistinct from noise."
            )

        self.execution_count += 1
        return {
            "status": "SUCCESS",
            "verdict": verdict,
            "is_significant": p_significant and ci_excludes_zero,
            "alpha": self.alpha,
            "p_value": p_val,
            "cohens_d": cohen_d,
            "effect_magnitude": effect_magnitude,
            "ci_95": [round(ci_low, 3), round(ci_high, 3)],
            "estimated_power": round(estimated_power, 3),
            "critique": critique
        }
