from __future__ import annotations

from pathlib import Path

import matplotlib
import pandas as pd


matplotlib.use("Agg")

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
INPUT_CSV = ROOT / "ansys" / "exported_results" / "mesh_convergence_raw.csv"
RESULTS_DIR = ROOT / "results"


def percent_change(series: pd.Series) -> pd.Series:
    return series.pct_change() * 100.0


def build_summary_table(df: pd.DataFrame) -> pd.DataFrame:
    summary = df.copy()
    summary["def_change_pct"] = percent_change(summary["max_def_mm"])
    summary["vm_change_pct"] = percent_change(summary["max_vm_mpa"])
    summary["principal_change_pct"] = percent_change(summary["max_principal_mpa"])
    summary["reaction_error_pct"] = (
        (summary["reaction_n"] - summary["reaction_n"].iloc[0]).abs()
        / summary["reaction_n"].iloc[0]
        * 100.0
    )
    return summary


def save_markdown_table(summary: pd.DataFrame, output_path: Path) -> None:
    columns = [
        "mesh_level",
        "global_size_mm",
        "nodes",
        "elements",
        "max_def_mm",
        "def_change_pct",
        "max_vm_mpa",
        "vm_change_pct",
        "max_principal_mpa",
        "principal_change_pct",
        "reaction_n",
        "reaction_error_pct",
    ]
    table = summary[columns].to_markdown(index=False, floatfmt=".5g")
    output_path.write_text(table + "\n", encoding="utf-8")


def save_metric_plot(
    summary: pd.DataFrame,
    metric: str,
    ylabel: str,
    output_path: Path,
) -> None:
    fig, ax = plt.subplots(figsize=(7.0, 4.2), dpi=160)
    ax.plot(
        summary["elements"],
        summary[metric],
        marker="o",
        linewidth=2.0,
        color="#1f6f8b",
    )
    for _, row in summary.iterrows():
        ax.annotate(
            row["mesh_level"].replace("_", " ").title(),
            (row["elements"], row[metric]),
            textcoords="offset points",
            xytext=(0, 8),
            ha="center",
            fontsize=8,
        )
    ax.set_xlabel("Elements")
    ax.set_ylabel(ylabel)
    ax.grid(True, alpha=0.3)
    ax.ticklabel_format(axis="x", style="plain")
    fig.tight_layout()
    fig.savefig(output_path)
    plt.close(fig)


def save_combined_plot(summary: pd.DataFrame, output_path: Path) -> None:
    normalized = summary.copy()
    metrics = {
        "max_def_mm": "Total deformation",
        "max_vm_mpa": "Von Mises stress",
        "max_principal_mpa": "Max principal stress",
    }

    fig, ax = plt.subplots(figsize=(7.0, 4.2), dpi=160)
    colors = ["#1f6f8b", "#b23a48", "#3f7d20"]
    for color, (metric, label) in zip(colors, metrics.items()):
        base = normalized[metric].iloc[-1]
        ax.plot(
            normalized["elements"],
            normalized[metric] / base,
            marker="o",
            linewidth=2.0,
            label=label,
            color=color,
        )

    ax.set_xlabel("Elements")
    ax.set_ylabel("Normalized to very fine mesh")
    ax.grid(True, alpha=0.3)
    ax.ticklabel_format(axis="x", style="plain")
    ax.legend(frameon=False)
    fig.tight_layout()
    fig.savefig(output_path)
    plt.close(fig)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(INPUT_CSV)
    df = df.sort_values("global_size_mm", ascending=False).reset_index(drop=True)
    summary = build_summary_table(df)

    summary.to_csv(RESULTS_DIR / "lc1_mesh_convergence_summary.csv", index=False)
    save_markdown_table(summary, RESULTS_DIR / "lc1_mesh_convergence_summary.md")
    save_metric_plot(
        summary,
        "max_def_mm",
        "Maximum total deformation [mm]",
        RESULTS_DIR / "lc1_deformation_convergence.png",
    )
    save_metric_plot(
        summary,
        "max_vm_mpa",
        "Maximum von Mises stress [MPa]",
        RESULTS_DIR / "lc1_von_mises_convergence.png",
    )
    save_metric_plot(
        summary,
        "max_principal_mpa",
        "Maximum principal stress [MPa]",
        RESULTS_DIR / "lc1_principal_stress_convergence.png",
    )
    save_combined_plot(summary, RESULTS_DIR / "lc1_normalized_convergence.png")

    print(f"Wrote LC1 mesh convergence outputs to {RESULTS_DIR}")


if __name__ == "__main__":
    main()
