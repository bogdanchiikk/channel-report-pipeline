import json
from pathlib import Path

import pandas as pd

DEFAULT_CONFIG = Path("config.example.json")


def load_config(path: str | Path = DEFAULT_CONFIG) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def load_metrics(path: str) -> dict:
    """Читает JSON канала и собирает таблицы для отчёта."""
    raw = json.loads(Path(path).read_text(encoding="utf-8"))

    daily = pd.DataFrame(raw.get("daily") or [])
    posts = pd.DataFrame(raw.get("posts") or [])

    start_subs = raw.get("start_subs")
    end_subs = raw.get("end_subs")
    if start_subs is None and not daily.empty and "subs_total" in daily.columns:
        start_subs = int(daily["subs_total"].iloc[0])
    if end_subs is None and not daily.empty and "subs_total" in daily.columns:
        end_subs = int(daily["subs_total"].iloc[-1])

    net_growth = raw.get("net_growth")
    if net_growth is None and start_subs is not None and end_subs is not None:
        net_growth = end_subs - start_subs

    gross_joined = raw.get("gross_joined")
    if gross_joined is None and not daily.empty and "joined" in daily.columns:
        gross_joined = int(daily["joined"].sum())

    return {
        "channel": raw.get("channel", ""),
        "period": raw.get("period", ""),
        "start_subs": start_subs,
        "end_subs": end_subs,
        "net_growth": net_growth,
        "gross_joined": gross_joined if gross_joined is not None else 0,
        "unsubs": raw.get("unsubs", 0),
        "daily": daily,
        "posts": posts,
    }


if __name__ == "__main__":
    config = load_config()
    metrics = load_metrics(config["sample"])
    print(metrics["channel"], metrics["period"])
    print("start/end/growth:", metrics["start_subs"], metrics["end_subs"], metrics["net_growth"])
    print("joined/left:", metrics["gross_joined"], metrics["unsubs"])
    print("days:", len(metrics["daily"]), "posts:", len(metrics["posts"]))
