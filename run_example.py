"""Run local synthetic checks, build and simulated deployment. Python stdlib only."""
import argparse
import json
from pathlib import Path
from core.artifact import build, digest
from adapters.simulated import SimulatedDeployment


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", required=True)
    parser.add_argument("--negative", action="store_true", help="intentionally corrupt candidate; exits nonzero")
    args = parser.parse_args()
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    baseline, candidate = build("v1"), build("v2")
    for name, data in [("v1.json", baseline), ("v2.json", candidate)]:
        (out / name).write_bytes(data)
        (out / (name + ".sha256")).write_text(digest(data) + "\n")
    adapter = SimulatedDeployment()
    adapter.deploy(baseline, digest(baseline), authorized=True)
    if args.negative:
        try:
            adapter.deploy(candidate + b"corrupt", digest(candidate), authorized=True)
        except ValueError:
            assert adapter.active == baseline
            print("EXPECTED REJECTION: corrupted artifact; baseline unchanged")
            return 2
        raise AssertionError("corruption was accepted")
    adapter.deploy(candidate, digest(candidate), authorized=True)
    adapter.rollback(authorized=True)
    assert adapter.active == baseline
    report = {"schema": 1, "scope": "synthetic-local-only", "state": "SIMULATED_ROLLBACK_VERIFIED",
              "baseline_sha256": digest(baseline), "candidate_sha256": digest(candidate),
              "rollback_equal": True, "real_deployment": False, "browser_e2e": "not_run",
              "independent_review_gate": "not_configured", "publication_authorized": False}
    (out / "result.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
