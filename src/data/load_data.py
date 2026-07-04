"""
Data loading module.

This module is responsible for reading the raw datasets.
"""

import pandas as pd

from src.utils.config import RAW_DATA_DIR
from src.utils.logger import logger


def load_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Load fake and true news datasets.

    Returns
    -------
    tuple[pd.DataFrame, pd.DataFrame]
        Fake news DataFrame and True news DataFrame.
    """

    logger.info("Loading Fake.csv...")

    fake_df = pd.read_csv(RAW_DATA_DIR / "Fake.csv")

    logger.info("Loading True.csv...")

    true_df = pd.read_csv(RAW_DATA_DIR / "True.csv")

    logger.info("Datasets loaded successfully.")

    return fake_df, true_df