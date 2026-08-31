from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def plot_subscribers(daily: pd.DataFrame, out_path) -> Path:
    """График числа подписчиков по дням. Пустая таблица — подпись No data, без ошибки."""
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(8, 3.2), dpi=140)
    ax.set_title("Subscribers by day")
    ax.set_xlabel("Day")
    ax.set_ylabel("Subscribers")

    if daily is None or daily.empty or "subs_total" not in daily.columns:
        ax.text(0.5, 0.5, "No data", ha="center", va="center", transform=ax.transAxes)
        ax.set_xticks([])
        ax.set_yticks([])
    else:
        ax.plot(daily["day"], daily["subs_total"], color="#2563EB", linewidth=2)
        ax.set_xlim(int(daily["day"].min()), int(daily["day"].max()))
        ax.grid(axis="y", linestyle="--", alpha=0.4)

    fig.tight_layout()
    fig.savefig(out_path, bbox_inches="tight")
    plt.close(fig)
    return out_path


if __name__ == "__main__":
    from metrics import load_metrics

    metrics = load_metrics("data/samples/channel_month.json")
    path = plot_subscribers(metrics["daily"], "output/subscribers.png")
    print("saved", path)
