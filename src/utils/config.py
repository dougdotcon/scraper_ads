"""
Configuration utilities for the Meta Ads Library Scraper.
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API Configuration
API_VERSION = "v19.0"  # Current Meta API version
API_BASE_URL = f"https://graph.facebook.com/{API_VERSION}/ads_archive"

# Default search parameters
DEFAULT_SEARCH_PARAMS = {
    "ad_type": "POLITICAL_AND_ISSUE_ADS",
    "ad_reached_countries": ["US"],
    "ad_active_status": "ACTIVE",
    "fields": "page_id,page_name,ad_snapshot_url,ad_creative_bodies,ad_delivery_start_time,ad_delivery_stop_time,currency,spend,impressions,demographic_distribution,publisher_platforms,bylines"
}

# UI Configuration
UI_TITLE = "Meta Ads Library Scraper"
UI_WIDTH = 1200
UI_HEIGHT = 800
UI_PADDING = 10

# Get API token from environment variable or return empty string
def get_api_token():
    """Get the API token from environment variables."""
    return os.getenv("META_ADS_API_TOKEN", "")

# Save API token to environment variables
def save_api_token(token):
    """Save the API token to the .env file."""
    with open(".env", "w") as f:
        f.write(f"META_ADS_API_TOKEN={token}")
    # Also update the current environment
    os.environ["META_ADS_API_TOKEN"] = token
