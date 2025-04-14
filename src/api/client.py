"""
Client for interacting with the Meta Ads Library API.
"""
import time
import json
import requests
from src.utils.config import API_BASE_URL, DEFAULT_SEARCH_PARAMS
from src.api.auth import AuthManager

class APIClient:
    """Client for the Meta Ads Library API."""
    
    def __init__(self, auth_manager=None):
        """Initialize with an optional auth manager."""
        self.auth_manager = auth_manager or AuthManager()
        self.rate_limit_remaining = None
        self.rate_limit_reset = None
        
    def set_auth_manager(self, auth_manager):
        """Set the authentication manager."""
        self.auth_manager = auth_manager
        
    def search_ads(self, params=None, max_pages=None):
        """
        Search for ads using the provided parameters.
        
        Args:
            params (dict): Search parameters to override defaults
            max_pages (int): Maximum number of pages to retrieve (None for all)
            
        Returns:
            list: List of ad data
        """
        if not self.auth_manager.get_token():
            raise ValueError("API token is required")
        
        # Merge default params with provided params
        search_params = DEFAULT_SEARCH_PARAMS.copy()
        if params:
            search_params.update(params)
        
        # Ensure access_token is included
        search_params['access_token'] = self.auth_manager.get_token()
        
        # Convert list parameters to JSON strings
        for key, value in search_params.items():
            if isinstance(value, list):
                search_params[key] = json.dumps(value)
        
        # Initialize results and pagination
        all_results = []
        next_url = API_BASE_URL
        page_count = 0
        
        while next_url and (max_pages is None or page_count < max_pages):
            try:
                # Make request
                if next_url == API_BASE_URL:
                    response = requests.get(next_url, params=search_params)
                else:
                    # For pagination, the URL already includes parameters
                    response = requests.get(next_url)
                
                # Check for rate limiting headers
                self._update_rate_limit_info(response)
                
                # Handle rate limiting
                if response.status_code == 429:
                    wait_time = self._get_rate_limit_wait_time()
                    print(f"Rate limited. Waiting {wait_time} seconds...")
                    time.sleep(wait_time)
                    continue
                
                # Check for errors
                if response.status_code != 200:
                    error_data = response.json().get('error', {})
                    error_message = error_data.get('message', 'Unknown error')
                    error_code = error_data.get('code', 'Unknown code')
                    raise Exception(f"API Error {error_code}: {error_message}")
                
                # Parse response
                data = response.json()
                
                # Add results
                if 'data' in data:
                    all_results.extend(data['data'])
                
                # Update pagination
                next_url = data.get('paging', {}).get('next')
                page_count += 1
                
                # Implement a small delay to be nice to the API
                time.sleep(0.5)
                
            except Exception as e:
                print(f"Error during API request: {e}")
                break
        
        return all_results
    
    def _update_rate_limit_info(self, response):
        """Update rate limit information from response headers."""
        # Meta API typically uses x-business-use-case-usage or x-app-usage headers
        # Format may vary, this is a simplified implementation
        if 'x-app-usage' in response.headers:
            try:
                usage_data = json.loads(response.headers['x-app-usage'])
                self.rate_limit_remaining = 100 - usage_data.get('call_count', 0)
                # Reset time is typically not provided directly
                self.rate_limit_reset = time.time() + 3600  # Assume 1 hour
            except:
                pass
    
    def _get_rate_limit_wait_time(self):
        """Calculate wait time based on rate limit information."""
        if self.rate_limit_reset:
            wait_time = max(0, self.rate_limit_reset - time.time())
            return min(wait_time, 3600)  # Cap at 1 hour
        return 60  # Default to 1 minute if no information available
