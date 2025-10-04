import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from typing import List, Optional, Tuple


def set_plot_style():
    """Apply a consistent matplotlib style used by the nanoplotting scripts.

    Call this once in a plotting session (optional). This avoids top-level
    side-effects on import.
    """
    plt.rcParams.update({
        "figure.figsize": (8, 6),
        "font.size": 14,
        "axes.linewidth": 1.5,
        "lines.linewidth": 2.5,
        "font.family": "sans-serif",
        "axes.prop_cycle": plt.cycler(color=[
            "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728",
            "#9467bd", "#8c564b", "#e377c2", "#7f7f7f",
            "#bcbd22", "#17becf"
        ])
    })


def read_combined_excel(
    filename: str,
    test_numbers: List[int],
    x_pattern: str,
    hardness_pattern: str,
    modulus_pattern: Optional[str] = None,
) -> pd.DataFrame:
    """Read an Excel file and combine multiple Test sheets into a single DataFrame.

    This function mirrors the behavior used by the plotting script but avoids
    any plotting or I/O side-effects beyond reading the Excel file.
    """
    combined_data = []

    try:
        excel_file = pd.ExcelFile(filename)

        for test_num in test_numbers:
            sheet_name = f"Test {test_num:03d}"
            if sheet_name in excel_file.sheet_names:
                sheet_data = pd.read_excel(filename, sheet_name=sheet_name)

                # Skip first row (units) if present
                if len(sheet_data) > 1:
                    sheet_data = sheet_data.iloc[1:].reset_index(drop=True)

                # Convert relevant columns to numeric where appropriate
                for col in sheet_data.columns:
                    if any(pattern in str(col) for pattern in [x_pattern, hardness_pattern, modulus_pattern or ""]):
                        sheet_data[col] = pd.to_numeric(sheet_data[col], errors='coerce')

                # Determine x column
                if x_pattern in sheet_data.columns:
                    x_col = x_pattern
                elif "Displacement Into Surface" in sheet_data.columns:
                    x_col = "Displacement Into Surface"
                else:
                    continue

                # Filter out invalid displacement rows
                valid_mask = (
                    pd.to_numeric(sheet_data[x_col], errors='coerce').notna() &
                    (pd.to_numeric(sheet_data[x_col], errors='coerce') > 0) &
                    (pd.to_numeric(sheet_data[x_col], errors='coerce') < 1000)
                )

                sheet_data = sheet_data[valid_mask].reset_index(drop=True)

                if len(sheet_data) > 0:
                    renamed_data = sheet_data.copy()
                    if "Hardness" in sheet_data.columns:
                        renamed_data[f'Test_{test_num}_{hardness_pattern}'] = sheet_data["Hardness"]
                    if modulus_pattern and "Modulus" in sheet_data.columns:
                        renamed_data[f'Test_{test_num}_{modulus_pattern}'] = sheet_data["Modulus"]
                    combined_data.append(renamed_data)

        if combined_data:
            result_df = pd.concat(combined_data, axis=0, ignore_index=True)
            return result_df
        else:
            # Return empty DataFrame if nothing found
            return pd.DataFrame()

    except Exception as e:
        # Surface the error but return empty DataFrame to avoid crashing callers
        print(f"Error reading {filename}: {e}")
        return pd.DataFrame()


def calculate_mean_std_count(df: pd.DataFrame, col_patterns: List[str]) -> Tuple[pd.Series, pd.Series, pd.Series]:
    """Return per-row mean, std (ddof=1), and count for columns matching patterns.

    The function coerces columns to numeric and ignores non-matching columns.
    """
    cols = [col for col in df.columns if any(pat in col for pat in col_patterns)]
    data = df[cols].apply(pd.to_numeric, errors='coerce')
    mean_values = data.mean(axis=1)
    std_values = data.std(axis=1, ddof=1)
    count_values = data.count(axis=1)
    return mean_values, std_values, count_values


def propagate_weighted_average_and_uncertainty(
    values: pd.Series, stds: pd.Series, counts: pd.Series
) -> Tuple[float, float]:
    """Propagate weighted average and uncertainty across results.

    Returns (weighted_mean, weighted_std). If inputs are invalid, returns (np.nan, np.nan).
    """
    values, stds, counts = values.dropna(), stds.dropna(), counts.dropna()
    if len(values) == 0 or not (len(values) == len(stds) == len(counts)):
        return np.nan, np.nan
    weighted_mean = np.sum(counts * values) / np.sum(counts)
    weighted_var = np.sum(counts * stds**2) / (np.sum(counts) ** 2)
    weighted_std = np.sqrt(weighted_var)
    return weighted_mean, weighted_std


def plot_curve_with_errors(ax, x_data, y_mean, y_std, idx, color, label, marker):
    """Plot a mean curve with error bars sampled at indices `idx`.

    This wraps matplotlib calls so callers don't have to duplicate the plotting
    details.
    """
    ax.plot(x_data, y_mean, color=color, label=label, linewidth=2.5)
    ax.errorbar(
        x_data.iloc[idx],
        y_mean.iloc[idx],
        yerr=y_std.iloc[idx],
        fmt=marker,
        markersize=6,
        linestyle='none',
        capsize=3,
        color=color,
        linewidth=1.5,
    )


__all__ = [
    'set_plot_style',
    'read_combined_excel',
    'calculate_mean_std_count',
    'propagate_weighted_average_and_uncertainty',
    'plot_curve_with_errors',
]
