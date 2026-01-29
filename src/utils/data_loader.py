"""
Utility functions for loading and preprocessing Typeform survey data.
"""

import pandas as pd
from pathlib import Path


def load_typeform_export(filepath: str | Path) -> pd.DataFrame:
    """
    Load a Typeform export file (CSV or Excel).

    Args:
        filepath: Path to the Typeform export file

    Returns:
        DataFrame with survey responses
    """
    filepath = Path(filepath)

    if filepath.suffix.lower() == '.csv':
        df = pd.read_csv(filepath)
    elif filepath.suffix.lower() in ['.xlsx', '.xls']:
        df = pd.read_excel(filepath)
    else:
        raise ValueError(f"Unsupported file format: {filepath.suffix}")

    return df


def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean Typeform column names for easier analysis.

    Args:
        df: DataFrame with original Typeform column names

    Returns:
        DataFrame with cleaned column names
    """
    df = df.copy()

    # Clean column names: lowercase, replace spaces with underscores
    df.columns = (
        df.columns
        .str.lower()
        .str.strip()
        .str.replace(r'[^\w\s]', '', regex=True)
        .str.replace(r'\s+', '_', regex=True)
    )

    return df


def get_response_summary(df: pd.DataFrame) -> dict:
    """
    Generate a summary of survey responses.

    Args:
        df: Survey response DataFrame

    Returns:
        Dictionary with summary statistics
    """
    return {
        'total_responses': len(df),
        'columns': list(df.columns),
        'missing_by_column': df.isnull().sum().to_dict(),
        'completion_rate': (1 - df.isnull().mean().mean()) * 100
    }
