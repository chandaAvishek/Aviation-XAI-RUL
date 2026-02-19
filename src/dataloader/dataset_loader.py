"""Dataset loader module for CMAPSS jet engine data."""

import os
from pathlib import Path
import pandas as pd

from src.config.config import DATA_DIR


def load_cmapss_data(filename: str) -> pd.DataFrame:
    """Load CMAPSS dataset from CSV file.
    
    Args:
        filename (str): Name of the dataset file (e.g., 'train_FD001.txt')
        
    Returns:
        pd.DataFrame: Loaded dataset with default column names (0, 1, 2, ...)
    """
    filepath = DATA_DIR / filename
    if not filepath.exists():
        raise FileNotFoundError(f"Dataset not found: {filepath}")
    
    return pd.read_csv(filepath, sep=" ", header=None)


# Example usage
if __name__ == "__main__":
    train_data = load_cmapss_data("train_FD001.txt")
    print(train_data.head())