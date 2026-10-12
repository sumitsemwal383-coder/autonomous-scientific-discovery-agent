"""
Command-Line Interface for Autonomous Scientific Discovery Agent
Executes end-to-end research pipelines from the terminal.
"""
import argparse
import json
import logging
import sys
from pathlib import Path

# Add project root to path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.agents.orchestrator import ScientificDiscoveryOrchestrator
from src.evaluation.benchmark_evaluator import BenchmarkEvaluator

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%H:%M:%S"
    )

def main():
    setup_logging()
    parser = argparse.ArgumentParser(description="Autonomous Multimodal Scientific Discovery Agent")
    parser.add_argument("--topic", type=str, default="multi-agent reinforcement learning reasoning", help="Research domain/topic")
    parser.add_argument("--max-papers", type=int, default=4, help="Maximum preprints to ingest from ArXiv and PubMed")
    parser.add_argument("--docker", action="store_true", help="Enable containerized Docker sandbox")
    parser.add_argument("--simulate-debug", action="store_true", help="Inject synthetic bug to demonstrate RL self-debugging")
    parser.add_argument("--output-json", type=str, default="", help="Path to export discovery result JSON")
    args = parser.parse_args()

    print("\n" + "="*75)
    print("  ZAALIMA DEVELOPMENT - ENTERPRISE DATA SCIENCE & ML")
    print("  PROJECT 1: AUTONOMOUS MULTIMODAL SCIENTIFIC DISCOVERY AGENT")
    print("="*75)
    print(f"[*] Target Research Topic: {args.topic}")
    print(f"[*] Sandbox Environment:  {'Docker Container' if args.docker else 'AST-Hardened Subprocess'}")
    print(f"[*] Simulating Self-Debug: {args.simulate_debug}")
    print("-"*75 + "\n")

    orchestrator = ScientificDiscoveryOrchestrator(
        use_docker=args.docker,
        max_debug_iterations=4
    )
    result = orchestrator.run_discovery_cycle(
        research_topic=args.topic,
        max_papers=args.max_papers,
        test_self_debug=args.simulate_debug
    )

    evaluator = BenchmarkEvaluator()
    bench = evaluator.evaluate_discovery_run(result)

    print("\n" + "="*75)
    print("  DISCOVERY CYCLE COMPLETED SUCCESSFULLY")
    print("="*75)
    print(f"Total Duration:     {result['duration_seconds']}s")
    print(f"Estimated Cost:     ${result['estimated_cost_usd']:.5f}")
    print(f"Hypothesis ID:      {result['hypothesis'].get('hypothesis_id')}")
    print(f"Critic Verdict:     {result['critic_evaluation'].get('verdict')}")
    print(f"p-value:            {result['code_execution'].get('metrics', {}).get('p_value', 1.0):.5e}")
    print(f"Cohen's d:          {result['code_execution'].get('metrics', {}).get('cohens_d', 0.0):.2f}")
    print(f"95% Conf Interval:  [{result['code_execution'].get('metrics', {}).get('ci_95_low', 0):.2f}, {result['code_execution'].get('metrics', {}).get('ci_95_high', 0):.2f}]")
    print(f"Holdout Benchmark:  {bench['overall_score']}% -> {bench['grade']}")
    print(f"LaTeX Paper:        {result['latex_synthesis'].get('tex_path')}")
    print("="*75 + "\n")

    if args.output_json:
        with open(args.output_json, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2)
        print(f"[+] Exported telemetry JSON to {args.output_json}")

if __name__ == "__main__":
    main()
