"""Unit tests for data loader."""

import sys
from pathlib import Path
import pytest

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.config import DATA_DIR


def test_data_dir_exists():
    """Test that data directory exists or can be created."""
    assert DATA_DIR.parent.exists(), "Project root should exist"


def test_project_structure():
    """Test that required src modules exist."""
    src_path = project_root / "src"
    assert (src_path / "__init__.py").exists(), "src/__init__.py should exist"
    assert (src_path / "dataloader").is_dir(), "src/dataloader should exist"
    assert (src_path / "config").is_dir(), "src/config should exist"


def test_config_imports():
    """Test that config module can be imported."""
    from src.config import PROJECT_ROOT, DATA_DIR, MODELS_DIR
    assert PROJECT_ROOT.exists(), "PROJECT_ROOT should exist"
    assert isinstance(DATA_DIR, Path), "DATA_DIR should be a Path"
    assert isinstance(MODELS_DIR, Path), "MODELS_DIR should be a Path"
