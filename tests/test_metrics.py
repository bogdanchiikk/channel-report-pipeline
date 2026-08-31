import json
from pathlib import Path

from src.metrics import load_metrics


def test_net_growth_fallback(tmp_path: Path):
    sample = {
        "channel": "MedChannel A",
        "period": "2026-07",
        "daily": [
            {"day": 1, "subs_total": 100, "joined": 2, "left": 0},
            {"day": 2, "subs_total": 130, "joined": 30, "left": 0},
        ],
        "posts": [],
    }
    path = tmp_path / "no_growth.json"
    path.write_text(json.dumps(sample), encoding="utf-8")
    metrics = load_metrics(str(path))
    assert metrics["start_subs"] == 100
    assert metrics["end_subs"] == 130
    assert metrics["net_growth"] == 30
    assert metrics["gross_joined"] == 32
