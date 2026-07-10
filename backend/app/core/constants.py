"""
Application-wide constants.

These values are used throughout the application and are not expected
to change between different environments.
"""

# ==========================
# API
# ==========================

API_V1_PREFIX = "/api/v1"

# ==========================
# Authentication
# ==========================

TOKEN_TYPE = "Bearer"

# ==========================
# Pagination
# ==========================

DEFAULT_PAGE_SIZE = 20
MAX_PAGE_SIZE = 100

# ==========================
# File Uploads
# ==========================

MAX_FILE_SIZE_MB = 5

ALLOWED_IMAGE_EXTENSIONS = (
    ".jpg",
    ".jpeg",
    ".png",
)

# ==========================
# Date & Time
# ==========================

DEFAULT_TIMEZONE = "UTC"