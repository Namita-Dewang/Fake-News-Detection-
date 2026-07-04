from pathlib import Path

# =============================================================================
# Project Root Directory
# =============================================================================

# config.py is located inside: src/utils/
# parents[2] moves up two levels:
# src/utils/config.py -> src -> project root
BASE_DIR = Path(__file__).resolve().parents[2]

# =============================================================================
# Data Directories
# =============================================================================

DATA_DIR = BASE_DIR / "data"

RAW_DATA_DIR = DATA_DIR / "raw"

INTERIM_DATA_DIR = DATA_DIR / "interim"

PROCESSED_DATA_DIR = DATA_DIR / "processed"

# =============================================================================
# Model Directory
# =============================================================================

MODEL_DIR = BASE_DIR / "saved_models"

# =============================================================================
# Reports Directory
# =============================================================================

REPORT_DIR = BASE_DIR / "reports"

FIGURE_DIR = REPORT_DIR / "figures"

METRIC_DIR = REPORT_DIR / "metrics"