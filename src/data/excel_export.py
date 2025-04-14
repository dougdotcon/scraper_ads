"""
Excel export functionality for Meta Ads Library data.
"""
import pandas as pd
from datetime import datetime

class ExcelExporter:
    """Exports data to Excel format."""
    
    def __init__(self):
        """Initialize the Excel exporter."""
        self.writer = None
        self.workbook = None
        
    def export_to_excel(self, data, search_params, filename=None):
        """
        Export data to Excel with multiple sheets.
        
        Args:
            data (list): List of processed ad data
            search_params (dict): Search parameters used
            filename (str): Output filename (default: auto-generated)
            
        Returns:
            str: Path to the saved Excel file
        """
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"meta_ads_export_{timestamp}.xlsx"
        
        # Create Excel writer
        with pd.ExcelWriter(filename, engine='openpyxl') as self.writer:
            self.workbook = self.writer.book
            
            # Create main data sheet
            self._create_main_data_sheet(data)
            
            # Create demographics sheet if data available
            if data and any(key.startswith('demo_') for key in data[0].keys()):
                self._create_demographics_sheet(data)
            
            # Create search parameters sheet
            self._create_search_params_sheet(search_params)
            
        return filename
    
    def _create_main_data_sheet(self, data):
        """Create the main data sheet."""
        # Filter out demographic columns for the main sheet
        main_columns = [col for col in data[0].keys() if not col.startswith('demo_')]
        
        # Create DataFrame with only main columns
        df = pd.DataFrame([{k: v for k, v in item.items() if k in main_columns} for item in data])
        
        # Rename columns for better readability
        column_mapping = {
            'id': 'Ad ID',
            'page_id': 'Page ID',
            'page_name': 'Page Name',
            'ad_snapshot_url': 'Ad URL',
            'ad_creative_body': 'Ad Text',
            'start_date': 'Start Date',
            'end_date': 'End Date',
            'currency': 'Currency',
            'spend': 'Spend',
            'impressions': 'Impressions',
            'platforms': 'Platforms',
            'byline': 'Paid By'
        }
        
        df = df.rename(columns=column_mapping)
        
        # Write to Excel
        df.to_excel(self.writer, sheet_name='Ad Data', index=False)
        
        # Auto-adjust column widths
        worksheet = self.writer.sheets['Ad Data']
        for i, col in enumerate(df.columns):
            max_width = max(
                df[col].astype(str).map(len).max(),
                len(col)
            )
            # Cap width at 50 characters
            adjusted_width = min(max_width + 2, 50)
            worksheet.column_dimensions[chr(65 + i)].width = adjusted_width
    
    def _create_demographics_sheet(self, data):
        """Create the demographics sheet."""
        # Extract only demographic columns
        demo_columns = [col for col in data[0].keys() if col.startswith('demo_')]
        
        if not demo_columns:
            return
            
        # Create DataFrame with demographic data and ad identifiers
        df = pd.DataFrame([
            {**{'Ad ID': item['id'], 'Page Name': item['page_name']}, 
             **{k: v for k, v in item.items() if k in demo_columns}}
            for item in data
        ])
        
        # Rename demographic columns for better readability
        column_mapping = {}
        for col in demo_columns:
            parts = col.replace('demo_', '').split('_')
            if len(parts) >= 2:
                age = parts[0].replace('plus', '+')
                gender = parts[1].capitalize()
                column_mapping[col] = f"{age} {gender}"
        
        df = df.rename(columns=column_mapping)
        
        # Write to Excel
        df.to_excel(self.writer, sheet_name='Demographics', index=False)
        
        # Auto-adjust column widths
        worksheet = self.writer.sheets['Demographics']
        for i, col in enumerate(df.columns):
            max_width = max(
                df[col].astype(str).map(len).max(),
                len(col)
            )
            worksheet.column_dimensions[chr(65 + i)].width = max_width + 2
    
    def _create_search_params_sheet(self, search_params):
        """Create a sheet with search parameters."""
        # Convert search parameters to a list of dictionaries
        params_list = [{'Parameter': k, 'Value': str(v)} for k, v in search_params.items()]
        
        # Create DataFrame
        df = pd.DataFrame(params_list)
        
        # Write to Excel
        df.to_excel(self.writer, sheet_name='Search Parameters', index=False)
        
        # Auto-adjust column widths
        worksheet = self.writer.sheets['Search Parameters']
        for i, col in enumerate(df.columns):
            max_width = max(
                df[col].astype(str).map(len).max(),
                len(col)
            )
            worksheet.column_dimensions[chr(65 + i)].width = max_width + 2
