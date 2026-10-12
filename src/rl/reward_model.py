"""
Reinforcement Learning Reward Model
Evaluates agent trajectory across syntax safety, execution fidelity, statistical significance,
and literature grounding.
"""
from typing import Dict, Any
from config.settings import (
    RL_REWARD_SYNTAX_PASS,
    RL_REWARD_EXEC_PASS,
    RL_REWARD_STAT_PASS,
    RL_REWARD_NOVELTY_PASS
)

class DiscoveryRewardModel:
    def __init__(self):
        self.w_syntax = RL_REWARD_SYNTAX_PASS
        self.w_exec = RL_REWARD_EXEC_PASS
        self.w_stat = RL_REWARD_STAT_PASS
        self.w_novelty = RL_REWARD_NOVELTY_PASS

    def compute_reward(
        self,
        syntax_valid: bool,
        execution_success: bool,
        is_breakout: bool,
        statistical_significance: bool,
        p_value: float,
        effect_size: float,
        grounded_in_lit: bool
    ) -> Dict[str, Any]:
        """
        Computes scalar reward in [-1.0, 1.0] and component score vectors.
        """
        # Critical security penalty for jailbreak/breakout attempts
        if is_breakout:
            return {
                "total_reward": -1.0,
                "components": {
                    "syntax_reward": -1.0,
                    "exec_reward": -1.0,
                    "stat_reward": 0.0,
                    "novelty_reward": 0.0
                },
                "verdict": "SECURITY_BREACH_PENALIZED"
            }

        r_syn = self.w_syntax if syntax_valid else -0.3
        r_exec = self.w_exec if execution_success else -0.2
        
        # Statistical reward: calibrated with p-value and effect size
        r_stat = 0.0
        if execution_success:
            if statistical_significance and p_value < 0.05:
                # Scaled by effect size strength
                bonus = min(0.1, effect_size * 0.1)
                r_stat = self.w_stat + bonus
            else:
                r_stat = 0.1  # Partial credit for running valid statistical test
        
        r_nov = self.w_novelty if grounded_in_lit else 0.0

        total = round(max(-1.0, min(1.0, r_syn + r_exec + r_stat + r_nov)), 4)

        return {
            "total_reward": total,
            "components": {
                "syntax_reward": round(r_syn, 3),
                "exec_reward": round(r_exec, 3),
                "stat_reward": round(r_stat, 3),
                "novelty_reward": round(r_nov, 3)
            },
            "verdict": "HIGH_VALUE_DISCOVERY" if total >= 0.7 else "ITERATIVE_REFINEMENT_NEEDED"
        }
