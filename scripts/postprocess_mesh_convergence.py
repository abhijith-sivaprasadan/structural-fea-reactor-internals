from __future__ import annotations

from pathlib import Path

import matplotlib
import pandas as pd


matplotlib.use("Agg")

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
INPUT_CSV = ROOT / "ansys" / "exported_results" / "mesh_convergence_raw.csv"
LOAD_CASE_SUMMARY_CSV = ROOT / "ansys" / "exported_results" / "load_case_summary.csv"
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


def save_load_case_outputs() -> None:
    if not LOAD_CASE_SUMMARY_CSV.exists():
        return

    summary = pd.read_csv(LOAD_CASE_SUMMARY_CSV)
    summary.to_markdown(
        RESULTS_DIR / "load_case_summary.md",
        index=False,
        floatfmt=".6g",
    )

    lc1 = summary.loc[summary["load_case"] == "LC1"].iloc[0]
    checks = []
    linear_scale_cases = summary.loc[
        (summary["load_case"] != "LC1")
        & (summary["force_y_n"] == lc1["force_y_n"])
        & (summary["force_z_n"] == lc1["force_z_n"])
    ]
    for _, row in linear_scale_cases.iterrows():
        scale_factor = row["force_x_n"] / lc1["force_x_n"]
        for source, label in [
            ("max_def_mm", "Max deformation [mm]"),
            ("max_vm_mpa", "Max von Mises stress [MPa]"),
            ("max_principal_mpa", "Max principal stress [MPa]"),
            ("reaction_total_n", "Reaction force resultant [N]"),
        ]:
            expected = lc1[source] * scale_factor
            checks.append(
                {
                    "load_case": row["load_case"],
                    "quantity": label,
                    "lc1_value": lc1[source],
                    "scale_factor": scale_factor,
                    "expected_value": expected,
                    "actual_value": row[source],
                    "difference_pct": (row[source] - expected) / expected * 100.0,
                }
            )

    scaling = pd.DataFrame(checks)
    if not scaling.empty:
        scaling.to_csv(RESULTS_DIR / "lc2_linear_scaling_check.csv", index=False)
        scaling.to_markdown(
            RESULTS_DIR / "lc2_linear_scaling_check.md",
            index=False,
            floatfmt=".6g",
        )

    force_balance = summary.copy()
    force_balance["expected_reaction_total_n"] = (
        force_balance["force_x_n"] ** 2
        + force_balance["force_y_n"] ** 2
        + force_balance["force_z_n"] ** 2
    ) ** 0.5
    force_balance["reaction_total_error_pct"] = (
        (force_balance["reaction_total_n"] - force_balance["expected_reaction_total_n"])
        / force_balance["expected_reaction_total_n"]
        * 100.0
    )
    force_balance.to_csv(RESULTS_DIR / "load_case_force_balance.csv", index=False)
    force_balance.to_markdown(
        RESULTS_DIR / "load_case_force_balance.md",
        index=False,
        floatfmt=".6g",
    )


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
    save_load_case_outputs()

    print(f"Wrote LC1 mesh convergence and load-case outputs to {RESULTS_DIR}")


if __name__ == "__main__":
    main()
