"""Project configuration and path management."""

from pathlib import Path

# Project root directory
PROJECT_ROOT = Path(__file__).parent.parent.parent
DATA_DIR = PROJECT_ROOT / "data"
NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"
MODELS_DIR = PROJECT_ROOT / "src" / "models"

# Dataset files
TRAIN_FILES = [
    "train_FD001.txt",
    "train_FD002.txt",
    "train_FD003.txt",
    "train_FD004.txt",
]
TEST_FILES = ["test_FD001.txt", "test_FD002.txt", "test_FD003.txt", "test_FD004.txt"]
RUL_FILES = ["RUL_FD001.txt", "RUL_FD002.txt", "RUL_FD003.txt", "RUL_FD004.txt"]

# Ensure directories exist
DATA_DIR.mkdir(parents=True, exist_ok=True)
MODELS_DIR.mkdir(parents=True, exist_ok=True)

__all__ = [
    "PROJECT_ROOT",
    "DATA_DIR",
    "NOTEBOOKS_DIR",
    "MODELS_DIR",
    "TRAIN_FILES",
    "TEST_FILES",
    "RUL_FILES",
]
