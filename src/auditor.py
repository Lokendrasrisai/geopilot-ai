import pandas as pd
import numpy as np
from src.rules import VERTICAL_RULES

def audit_dataframe(df: pd.DataFrame, vertical: str):
    rules = VERTICAL_RULES[vertical]

    total_rows = len(df)
    total_cols = len(df.columns)
    missing_total = int(df.isna().sum().sum())
    duplicate_rows = int(df.duplicated().sum())
    missing_ratio = float(missing_total / max(total_rows * max(total_cols, 1), 1))

    missing_by_col = (df.isna().mean().sort_values(ascending=False) * 100).round(2)
    high_missing_cols = missing_by_col[missing_by_col >= 20].to_dict()

    critical_missing = [c for c in rules["critical_fields"] if c not in df.columns]
    recommended_missing = [c for c in rules["recommended_fields"] if c not in df.columns]

    suspicious_term_hits = []
    for col in df.columns:
        if df[col].dtype == "object":
            col_series = df[col].fillna("").astype(str).str.lower()
            for term in rules["high_risk_terms"]:
                count = int((col_series == term).sum())
                if count > 0:
                    suspicious_term_hits.append({"column": col, "term": term, "count": count})

    numeric_outlier_flags = []
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    for col in numeric_cols:
        series = df[col].dropna()
        if len(series) >= 10:
            q1, q3 = series.quantile(0.25), series.quantile(0.75)
            iqr = q3 - q1
            low, high = q1 - 1.5 * iqr, q3 + 1.5 * iqr
            outlier_count = int(((series < low) | (series > high)).sum())
            if outlier_count > 0:
                numeric_outlier_flags.append({"column": col, "outlier_count": outlier_count})

    coordinate_flags = {}
    if "latitude" in df.columns:
        invalid_lat = int((pd.to_numeric(df["latitude"], errors="coerce").dropna().abs() > 90).sum())
        if invalid_lat > 0:
            coordinate_flags["invalid_latitude_count"] = invalid_lat
    if "longitude" in df.columns:
        invalid_lon = int((pd.to_numeric(df["longitude"], errors="coerce").dropna().abs() > 180).sum())
        if invalid_lon > 0:
            coordinate_flags["invalid_longitude_count"] = invalid_lon

    staleness_signal = 0
    for c in ["updated_at", "inspection_date"]:
        if c in df.columns:
            staleness_signal += int(df[c].isna().sum())

    issue_count = (
        len(critical_missing) * 12
        + len(recommended_missing) * 4
        + duplicate_rows * 1
        + int(missing_ratio * 100)
        + len(suspicious_term_hits) * 2
        + len(numeric_outlier_flags) * 2
        + sum(coordinate_flags.values())
    )

    readiness = max(0, min(100, 100 - issue_count))

    severity = "Low"
    if readiness < 80:
        severity = "Medium"
    if readiness < 60:
        severity = "High"
    if readiness < 40:
        severity = "Critical"

    return {
        "summary": {
            "rows": total_rows,
            "columns": total_cols,
            "missing_cells": missing_total,
            "duplicate_rows": duplicate_rows,
            "missing_ratio_pct": round(missing_ratio * 100, 2),
            "readiness_score": readiness,
            "severity": severity,
            "staleness_signal": staleness_signal,
        },
        "critical_missing_fields": critical_missing,
        "recommended_missing_fields": recommended_missing,
        "high_missing_columns": high_missing_cols,
        "suspicious_terms": suspicious_term_hits[:20],
        "numeric_outliers": numeric_outlier_flags[:20],
        "coordinate_flags": coordinate_flags,
    }
