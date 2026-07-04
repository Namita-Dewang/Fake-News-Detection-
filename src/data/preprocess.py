"""
Dataset preparation module.

Creates a single labeled dataset from Fake.csv and True.csv.
"""

import pandas as pd

from src.utils.config import INTERIM_DATA_DIR
from src.utils.logger import logger


def create_master_dataset(
    fake_df: pd.DataFrame,
    true_df: pd.DataFrame
) -> pd.DataFrame:
    """
    Create the master dataset.

    Parameters
    ----------
    fake_df : pd.DataFrame
    true_df : pd.DataFrame

    Returns
    -------
    pd.DataFrame
    """

    logger.info("Adding labels...")

    fake_df = fake_df.copy()
    true_df = true_df.copy()

    fake_df["label"] = 0
    true_df["label"] = 1

    logger.info("Merging datasets...")

    news_df = pd.concat(
        [fake_df, true_df],
        ignore_index=True
    )

    logger.info("Shuffling dataset...")

    news_df = news_df.sample(
        frac=1,
        random_state=42
    ).reset_index(drop=True)

    logger.info("Saving dataset...")

    INTERIM_DATA_DIR.mkdir(exist_ok=True)

    output_path = INTERIM_DATA_DIR / "news.csv"

    news_df.to_csv(
        output_path,
        index=False
    )

    logger.info(f"Dataset saved to: {output_path}")

    return news_df