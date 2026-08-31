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


def plot_joins_unsubs(daily: pd.DataFrame, out_path) -> Path:
    """Столбики: сколько пришло (joined) и ушло (left) в каждый день."""
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(8, 3.2), dpi=140)
    ax.set_title("Joined vs left by day")
    ax.set_xlabel("Day")
    ax.set_ylabel("People")

    has_cols = (
        daily is not None
        and not daily.empty
        and "joined" in daily.columns
        and "left" in daily.columns
    )
    if not has_cols:
        ax.text(0.5, 0.5, "No data", ha="center", va="center", transform=ax.transAxes)
        ax.set_xticks([])
        ax.set_yticks([])
    else:
        ax.bar(daily["day"] - 0.2, daily["joined"], width=0.4, label="Joined", color="#16A34A")
        ax.bar(daily["day"] + 0.2, daily["left"], width=0.4, label="Left", color="#DC2626")
        ax.legend()
        ax.grid(axis="y", linestyle="--", alpha=0.4)

    fig.tight_layout()
    fig.savefig(out_path, bbox_inches="tight")
    plt.close(fig)
    return out_path


if __name__ == "__main__":
    from metrics import load_metrics

    metrics = load_metrics("data/samples/channel_month.json")
    p1 = plot_subscribers(metrics["daily"], "output/subscribers.png")
    p2 = plot_joins_unsubs(metrics["daily"], "output/joins_unsubs.png")
    print("saved", p1)
    print("saved", p2)
