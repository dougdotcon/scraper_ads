"""
Authentication module for Meta Ads Library API.
"""
import requests
from src.utils.config import API_BASE_URL

class AuthManager:
    """Manages authentication for the Meta Ads Library API."""
    
    def __init__(self, token=None):
        """Initialize with optional token."""
        self.token = token
        
    def set_token(self, token):
        """Set the API token."""
        self.token = token
        
    def get_token(self):
        """Get the current API token."""
        return self.token
    
    def validate_token(self):
        """
        Validate the API token by making a simple request.
        Returns True if valid, False otherwise.
        """
        if not self.token:
            return False
        
        try:
            # Make a minimal request to check if token is valid
            params = {
                'access_token': self.token,
                'limit': 1,
                'ad_type': 'POLITICAL_AND_ISSUE_ADS',
                'ad_reached_countries': '["US"]'
            }
            
            response = requests.get(API_BASE_URL, params=params)
            
            # Check if response is successful
            if response.status_code == 200:
                return True
            
            # Check for specific error codes related to invalid tokens
            error_data = response.json().get('error', {})
            error_code = error_data.get('code')
            
            # Log the error for debugging
            print(f"Token validation failed: {error_data}")
            
            return False
            
        except Exception as e:
            print(f"Error validating token: {e}")
            return False
