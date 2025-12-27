# MetaAdsLibraryScraper

A robust Python-based tool with a graphical interface for extracting and analyzing advertising data from the Meta Ads Library API. It simplifies data retrieval through customizable search filters and enables export to Excel for comprehensive analysis.

![Meta Ads Library Scraper](assets/icons/app_preview.png)

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage Guide](#usage-guide)
  - [API Configuration](#api-configuration)
  - [Searching for Ads](#searching-for-ads)
  - [Data Visualization & Export](#data-visualization--export)
- [Search Parameters](#search-parameters)
- [Troubleshooting](#troubleshooting)
- [FAQ](#faq)

## Overview

The MetaAdsLibraryScraper is designed for marketers, researchers, and developers who need to interact with the Meta Ads Library API without dealing with complex command-line tools. It provides a streamlined, user-friendly way to fetch ad creatives, copy, and metadata based on specific criteria.

## Features

- **Intuitive GUI**: Built with Python's `tkinter` for easy navigation.
- **Advanced Filtering**: Filter ads by keywords, country, date range, platforms, and ad type.
- **Data Export**: Save results directly to `.xlsx` (Excel) format for further analysis.
- **Token Management**: Securely save and validate your Meta API access token.
- **Real-time Monitoring**: Track the scraping progress directly in the interface.

## Prerequisites

- Python 3.7+
- Internet connection
- Meta for Developers account (for API access token)
- Python libraries (automatically installed via `requirements.txt`):
  - `tkinter`
  - `requests`
  - `pandas`
  - `openpyxl`
  - `python-dotenv`
  - `Pillow`

## Installation

1. **Clone the repository:**
   bash
   git clone https://github.com/yourusername/scraper_ads.git
   cd scraper_ads
   

2. **Install dependencies:**
   bash
   pip install -r requirements.txt
   

3. **Run the application:**
   bash
   python main.py
   

## Usage Guide

### API Configuration

Before searching, you must configure your Meta API token:

1. Upon launching the app, navigate to the **Configuration** tab.
2. Obtain your Access Token from the [Meta for Developers Portal](https://developers.facebook.com/).
   - Ensure the token has the `ads_read` permission.
3. Paste the token into the "Access Token" field.
4. Click **Save Token** to store it locally.
5. Click **Validate Token** to verify connectivity.

### Searching for Ads

1. Switch to the **Search** tab.
2. Enter your search criteria:
   - **Search Terms**: Keywords to look for in ad text.
   - **Ad Type**: Specific categories (e.g., Political, Housing, Employment).
   - **Countries**: Comma-separated country codes (e.g., `US, BR, CA`).
   - **Date Range**: Start and end dates for the ad run period.
   - **Platforms**: Where the ads appeared (Facebook, Instagram, Audience Network).
   - **Ad Status**: Active, Inactive, or All.
3. Click **Search Ads** to initiate the data extraction.

### Data Visualization & Export

- View results in the **Results** tab, where ads are listed with their respective details.
- Click on a specific ad entry to view creative details (if available).
- Use the **Export to Excel** button to save the full dataset to a spreadsheet.

## Search Parameters

The tool utilizes the official Meta Ads Library API endpoints. Key parameters include:

- `search_terms`: String for keyword matching.
- `ad_reached_countries`: List of ISO 3166-1 alpha-2 country codes.
- `ad_type`: Options include `ALL`, `POLITICAL_AND_ISSUE_ADVERTISING`, `HOUSING`, `EMPLOYMENT`, `CREDIT`.
- `start_date` / `end_date`: Format `YYYY-MM-DD`.
- `platforms`: List of platforms like `FACEBOOK`, `INSTAGRAM`.

## Troubleshooting

- **"Token Invalid" Error**: Ensure your token has not expired and includes the `ads_read` permission.
- **No Results Found**: Broaden your search terms or remove country filters. Note that the API might not return data for very specific/low-volume queries.
- **App Crashes on Start**: Ensure `tkinter` is installed (it is often included with Python, but may require separate installation on Linux: `sudo apt-get install python3-tk`).

## FAQ

**Q: Is this tool free to use?**
A: Yes, the software is open source. However, usage of the Meta API is subject to Meta's [Platform Terms](https://developers.facebook.com/terms) and data usage policies.

**Q: Does this scrape data without API access?**
A: No, this tool relies entirely on the official Meta Ads Library API. You must have a valid access token.

**Q: Can I download the actual ad images?**
A: The API provides links to media assets. The tool allows you to export these links, but bulk downloading images may require specific configurations or additional tools due to API rate limits.