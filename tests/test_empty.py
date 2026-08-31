import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.metrics import load_metrics


def test_empty_month():
    metrics = load_metrics("data/samples/empty_month.json")
    assert metrics["channel"] == "MedChannel A"
    assert len(metrics["daily"]) == 0
    assert len(metrics["posts"]) == 0
    print("empty sample: ok, no crash")


if __name__ == "__main__":
    test_empty_month()
