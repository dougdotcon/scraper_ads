"""
Results frame for the Meta Ads Library Scraper.
"""
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import webbrowser
from src.data.excel_export import ExcelExporter
from src.gui.styles import COLORS, FONTS, PADDING, BUTTON_STYLES, ENTRY_STYLES, FRAME_STYLES, LABEL_STYLES

class ResultsFrame(ttk.Frame):
    """Frame for displaying search results."""
    
    def __init__(self, parent):
        """Initialize the results frame."""
        super().__init__(parent, padding=PADDING["medium"])
        
        self.parent = parent
        self.current_data = []
        self.current_search_params = {}
        self.excel_exporter = ExcelExporter()
        
        self._create_widgets()
        self._layout_widgets()
    
    def _create_widgets(self):
        """Create the widgets for the results frame."""
        # Title and controls
        self.header_frame = ttk.Frame(self)
        
        self.title_label = ttk.Label(
            self.header_frame, 
            text="Search Results", 
            font=FONTS["header"],
            foreground=COLORS["primary"]
        )
        
        self.export_button = ttk.Button(
            self.header_frame,
            text="Export to Excel",
            command=self._export_to_excel,
            state="disabled",
            style="Accent.TButton"
        )
        
        # Results count
        self.count_label = ttk.Label(
            self, 
            text="No results to display", 
            font=FONTS["normal"]
        )
        
        # Results table
        self.table_frame = ttk.Frame(self)
        
        # Create treeview with scrollbars
        self.tree_columns = [
            "page_name", "ad_creative_body", "start_date", 
            "spend", "impressions", "platforms"
        ]
        
        self.tree_headings = {
            "page_name": "Page Name",
            "ad_creative_body": "Ad Text",
            "start_date": "Start Date",
            "spend": "Spend",
            "impressions": "Impressions",
            "platforms": "Platforms"
        }
        
        self.tree = ttk.Treeview(
            self.table_frame,
            columns=self.tree_columns,
            show="headings",
            selectmode="browse",
            height=20
        )
        
        # Configure columns and headings
        for col in self.tree_columns:
            self.tree.heading(col, text=self.tree_headings[col])
            
            # Set column widths
            if col == "ad_creative_body":
                self.tree.column(col, width=300, stretch=True)
            elif col == "page_name":
                self.tree.column(col, width=150, stretch=True)
            else:
                self.tree.column(col, width=100, stretch=False)
        
        # Add scrollbars
        self.vsb = ttk.Scrollbar(
            self.table_frame, 
            orient="vertical", 
            command=self.tree.yview
        )
        self.hsb = ttk.Scrollbar(
            self.table_frame, 
            orient="horizontal", 
            command=self.tree.xview
        )
        self.tree.configure(yscrollcommand=self.vsb.set, xscrollcommand=self.hsb.set)
        
        # Bind double-click to open ad
        self.tree.bind("<Double-1>", self._on_item_double_click)
        
        # Details frame
        self.details_frame = ttk.LabelFrame(
            self,
            text="Ad Details",
            padding=PADDING["medium"]
        )
        
        self.details_text = tk.Text(
            self.details_frame,
            wrap="word",
            width=50,
            height=10,
            font=FONTS["normal"],
            state="disabled"
        )
        
        self.details_scroll = ttk.Scrollbar(
            self.details_frame,
            orient="vertical",
            command=self.details_text.yview
        )
        self.details_text.configure(yscrollcommand=self.details_scroll.set)
        
        self.open_ad_button = ttk.Button(
            self.details_frame,
            text="Open Ad in Browser",
            command=self._open_selected_ad,
            state="disabled"
        )
    
    def _layout_widgets(self):
        """Layout the widgets in the frame."""
        # Header frame
        self.header_frame.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(0, PADDING["medium"]))
        self.title_label.pack(side="left")
        self.export_button.pack(side="right")
        
        # Results count
        self.count_label.grid(row=1, column=0, columnspan=2, sticky="w", pady=(0, PADDING["small"]))
        
        # Results table
        self.table_frame.grid(row=2, column=0, sticky="nsew", pady=PADDING["small"])
        self.tree.grid(row=0, column=0, sticky="nsew")
        self.vsb.grid(row=0, column=1, sticky="ns")
        self.hsb.grid(row=1, column=0, sticky="ew")
        
        # Configure table frame grid
        self.table_frame.rowconfigure(0, weight=1)
        self.table_frame.columnconfigure(0, weight=1)
        
        # Details frame
        self.details_frame.grid(row=2, column=1, sticky="nsew", padx=(PADDING["medium"], 0), pady=PADDING["small"])
        self.details_text.grid(row=0, column=0, sticky="nsew")
        self.details_scroll.grid(row=0, column=1, sticky="ns")
        self.open_ad_button.grid(row=1, column=0, sticky="w", pady=(PADDING["medium"], 0))
        
        # Configure details frame grid
        self.details_frame.rowconfigure(0, weight=1)
        self.details_frame.columnconfigure(0, weight=1)
        
        # Configure main grid
        self.rowconfigure(2, weight=1)
        self.columnconfigure(0, weight=3)
        self.columnconfigure(1, weight=1)
        
        # Bind selection event
        self.tree.bind("<<TreeviewSelect>>", self._on_item_select)
    
    def update_results(self, data, search_params):
        """Update the results with new data."""
        self.current_data = data
        self.current_search_params = search_params
        
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Update count label
        if data:
            self.count_label.config(text=f"Displaying {len(data)} results")
            self.export_button.config(state="normal")
        else:
            self.count_label.config(text="No results to display")
            self.export_button.config(state="disabled")
        
        # Add data to treeview
        for i, item in enumerate(data):
            # Truncate ad text for display
            ad_text = item.get("ad_creative_body", "")
            if len(ad_text) > 100:
                ad_text = ad_text[:97] + "..."
            
            # Format values for display
            values = [
                item.get("page_name", ""),
                ad_text,
                item.get("start_date", ""),
                item.get("spend", ""),
                item.get("impressions", ""),
                item.get("platforms", "")
            ]
            
            # Insert into treeview with the item's index as the iid
            self.tree.insert("", "end", iid=str(i), values=values)
    
    def _on_item_select(self, event):
        """Handle item selection in the treeview."""
        selection = self.tree.selection()
        if not selection:
            return
        
        # Get the selected item's index
        index = int(selection[0])
        if index < 0 or index >= len(self.current_data):
            return
        
        # Get the selected item's data
        item = self.current_data[index]
        
        # Update details text
        self.details_text.config(state="normal")
        self.details_text.delete(1.0, tk.END)
        
        # Format details
        details = [
            f"Page: {item.get('page_name', 'N/A')}",
            f"Ad ID: {item.get('id', 'N/A')}",
            f"Start Date: {item.get('start_date', 'N/A')}",
            f"End Date: {item.get('end_date', 'N/A') or 'Active'}",
            f"Spend: {item.get('spend', 'N/A')}",
            f"Impressions: {item.get('impressions', 'N/A')}",
            f"Platforms: {item.get('platforms', 'N/A')}",
            f"Paid By: {item.get('byline', 'N/A')}",
            "\nAd Text:",
            item.get("ad_creative_body", "N/A")
        ]
        
        self.details_text.insert(tk.END, "\n".join(details))
        self.details_text.config(state="disabled")
        
        # Enable open ad button if URL is available
        if item.get("ad_snapshot_url"):
            self.open_ad_button.config(state="normal")
        else:
            self.open_ad_button.config(state="disabled")
    
    def _on_item_double_click(self, event):
        """Handle double-click on an item."""
        self._open_selected_ad()
    
    def _open_selected_ad(self):
        """Open the selected ad in a browser."""
        selection = self.tree.selection()
        if not selection:
            return
        
        # Get the selected item's index
        index = int(selection[0])
        if index < 0 or index >= len(self.current_data):
            return
        
        # Get the ad URL
        ad_url = self.current_data[index].get("ad_snapshot_url")
        if not ad_url:
            messagebox.showerror("Error", "No URL available for this ad")
            return
        
        # Open in browser
        webbrowser.open(ad_url)
    
    def _export_to_excel(self):
        """Export the current results to Excel."""
        if not self.current_data:
            messagebox.showerror("Error", "No data to export")
            return
        
        # Ask for save location
        file_path = filedialog.asksaveasfilename(
            defaultextension=".xlsx",
            filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")],
            title="Save Excel File"
        )
        
        if not file_path:
            return  # User cancelled
        
        try:
            # Export data
            self.excel_exporter.export_to_excel(
                self.current_data,
                self.current_search_params,
                file_path
            )
            
            messagebox.showinfo("Success", f"Data exported successfully to {file_path}")
            
        except Exception as e:
            messagebox.showerror("Export Error", f"Failed to export data: {str(e)}")
