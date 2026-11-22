"""
Data Loader Module
Provides functions to load datasets, perform schema verification, and run data quality audits.
"""

import os
import pandas as pd
import numpy as np
from typing import Dict, Any, Tuple


def load_dataset(filepath: str, parse_dates: list = None) -> pd.DataFrame:
    """
    Load a CSV dataset with error handling and basic checks.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Dataset not found at path: {filepath}")
    
    df = pd.read_csv(filepath, parse_dates=parse_dates)
    return df


def audit_data_quality(df: pd.DataFrame, dataset_name: str = "Dataset") -> Dict[str, Any]:
    """
    Perform a comprehensive data quality audit.
    Returns dictionary of health metrics.
    """
    total_rows, total_cols = df.shape
    missing_counts = df.isnull().sum()
    total_missing = int(missing_counts.sum())
    duplicate_rows = int(df.duplicated().sum())
    memory_usage_mb = round(df.memory_usage(deep=True).sum() / (1024 * 1024), 2)
    
    column_stats = {}
    for col in df.columns:
        col_type = str(df[col].dtype)
        null_count = int(df[col].isnull().sum())
        null_pct = round((null_count / total_rows) * 100, 2)
        unique_count = int(df[col].nunique())
        column_stats[col] = {
            "dtype": col_type,
            "null_count": null_count,
            "null_pct": null_pct,
            "unique_count": unique_count
        }
        
    audit_report = {
        "dataset_name": dataset_name,
        "total_rows": total_rows,
        "total_columns": total_cols,
        "total_missing_values": total_missing,
        "duplicate_rows": duplicate_rows,
        "memory_usage_mb": memory_usage_mb,
        "columns": column_stats
    }
    return audit_report


def print_audit_summary(audit: Dict[str, Any]) -> None:
    """Print readable audit report to console."""
    print("=" * 60)
    print(f"DATA QUALITY AUDIT: {audit['dataset_name']}")
    print("=" * 60)
    print(f"Dimensions: {audit['total_rows']:,} rows × {audit['total_columns']} columns")
    print(f"Missing Values: {audit['total_missing_values']} total")
    print(f"Duplicate Rows: {audit['duplicate_rows']}")
    print(f"Memory Footprint: {audit['memory_usage_mb']} MB")
    print("-" * 60)
    print(f"{'Column':<25} {'Type':<12} {'Missing':<10} {'Unique':<8}")
    print("-" * 60)
    for col, stats in audit['columns'].items():
        print(f"{col:<25} {stats['dtype']:<12} {stats['null_count']} ({stats['null_pct']}%) {stats['unique_count']}")
    print("=" * 60)
