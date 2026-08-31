from src.metrics import load_metrics


def test_empty_month():
    metrics = load_metrics("data/samples/empty_month.json")
    assert metrics["channel"] == "MedChannel A"
    assert len(metrics["daily"]) == 0
    assert len(metrics["posts"]) == 0
