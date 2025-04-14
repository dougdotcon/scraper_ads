"""
Data processor for Meta Ads Library API results.
"""
import json

class DataProcessor:
    """Processes data from the Meta Ads Library API."""
    
    def __init__(self):
        """Initialize the data processor."""
        self.raw_data = []
        self.processed_data = []
        
    def process_ads_data(self, ads_data):
        """
        Process raw ads data from the API.
        
        Args:
            ads_data (list): List of ad data from the API
            
        Returns:
            list: Processed data
        """
        self.raw_data = ads_data
        self.processed_data = []
        
        for ad in ads_data:
            processed_ad = self._process_single_ad(ad)
            self.processed_data.append(processed_ad)
            
        return self.processed_data
    
    def _process_single_ad(self, ad):
        """Process a single ad record."""
        processed = {
            'id': ad.get('id', ''),
            'page_id': ad.get('page_id', ''),
            'page_name': ad.get('page_name', ''),
            'ad_snapshot_url': ad.get('ad_snapshot_url', ''),
            'ad_creative_body': self._join_list_field(ad, 'ad_creative_bodies'),
            'start_date': ad.get('ad_delivery_start_time', ''),
            'end_date': ad.get('ad_delivery_stop_time', ''),
            'currency': ad.get('currency', ''),
            'spend': self._extract_range_value(ad.get('spend', {})),
            'impressions': self._extract_range_value(ad.get('impressions', {})),
            'platforms': ', '.join(ad.get('publisher_platforms', [])),
            'byline': ad.get('bylines', ''),
        }
        
        # Process demographic data if available
        if 'demographic_distribution' in ad:
            demographics = self._process_demographics(ad['demographic_distribution'])
            processed.update(demographics)
            
        return processed
    
    def _join_list_field(self, ad, field_name, separator='\n'):
        """Join a list field into a single string."""
        if field_name in ad and isinstance(ad[field_name], list):
            return separator.join(ad[field_name])
        return ''
    
    def _extract_range_value(self, range_data):
        """Extract a human-readable value from a range object."""
        if not range_data:
            return ''
            
        if isinstance(range_data, str):
            return range_data
            
        if isinstance(range_data, dict):
            lower = range_data.get('lower_bound', '')
            upper = range_data.get('upper_bound', '')
            
            if lower and upper:
                return f"{lower}-{upper}"
            elif lower:
                return f">{lower}"
            elif upper:
                return f"<{upper}"
                
        return str(range_data)
    
    def _process_demographics(self, demographic_data):
        """Process demographic distribution data."""
        result = {}
        
        for item in demographic_data:
            age = item.get('age', '')
            gender = item.get('gender', '')
            percentage = item.get('percentage', '')
            
            key = f"demo_{age}_{gender}".lower().replace('+', 'plus')
            result[key] = percentage
            
        return result
    
    def get_preview_data(self, limit=10):
        """Get a preview of the processed data."""
        return self.processed_data[:limit]
    
    def get_all_data(self):
        """Get all processed data."""
        return self.processed_data
