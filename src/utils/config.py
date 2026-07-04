from pathlib import Path

# Project root
BASE_DIR = Path(__file__).resolve().parent

# Data directories
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

# Models directory
MODEL_DIR = BASE_DIR / "saved_models"

# Reports directory
REPORT_DIR = BASE_DIR / "reports"