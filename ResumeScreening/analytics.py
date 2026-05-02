import pandas as pd
import numpy as np
from pandas import DataFrame


def create_candidate_dataframe(candidate_data: list[dict]) -> DataFrame:
    return pd.DataFrame(candidate_data)


def calculate_score_statistics(df: DataFrame) -> dict:
    if df.empty:
        return {
            "average_score": 0.0,
            "highest_score": 0.0,
            "lowest_score": 0.0,
            "total_candidates": 0,
        }

    scores = df["Resume Score"].to_numpy(dtype=float)

    return {
        "average_score": float(np.mean(scores)),
        "highest_score": float(np.max(scores)),
        "lowest_score": float(np.min(scores)),
        "total_candidates": int(len(scores)),
    }


def get_top_candidates(df: DataFrame, top_n: int = 3) -> DataFrame:
    if df.empty:
        return df
    return df.sort_values(by="Resume Score", ascending=False).head(top_n)

