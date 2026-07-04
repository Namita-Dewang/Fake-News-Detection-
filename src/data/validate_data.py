"""
Data validation module.
"""

import pandas as pd

from src.utils.logger import logger

# Columns that must exist
REQUIRED_COLUMNS = ["title", "text", "subject", "date"]


def validate_dataframe(df: pd.DataFrame, dataset_name: str) -> None:
    """
    Validate a news dataset.

    Parameters
    ----------
    df : pd.DataFrame
        Dataset to validate.

    dataset_name : str
        Name used in log messages.
    """

    logger.info(f"Validating {dataset_name} dataset...")

    # Check if dataset is empty
    if df.empty:
        raise ValueError(f"{dataset_name} dataset is empty.")

    logger.info(f"Shape: {df.shape}")

    # Check required columns
    missing_columns = [
        column for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing columns in {dataset_name}: {missing_columns}"
        )

    logger.info("All required columns are present.")

    # Check missing values
    missing_values = df.isnull().sum()

    logger.info("Missing Values:")
    logger.info(f"\n{missing_values}")

    # Check duplicates
    duplicate_count = df.duplicated().sum()

    logger.info(f"Duplicate Rows: {duplicate_count}")

    # Data types
    logger.info("Data Types:")
    logger.info(f"\n{df.dtypes}")

    logger.info(f"{dataset_name} validation completed successfully.\n")