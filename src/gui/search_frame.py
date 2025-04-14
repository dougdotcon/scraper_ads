"""
Search frame for the Meta Ads Library Scraper.
"""
import tkinter as tk
from tkinter import ttk, messagebox
import json
from datetime import datetime, timedelta
from src.gui.styles import COLORS, FONTS, PADDING, BUTTON_STYLES, ENTRY_STYLES, FRAME_STYLES, LABEL_STYLES

class SearchFrame(ttk.Frame):
    """Frame for search parameters and filters."""

    def __init__(self, parent, api_client, data_processor, on_search_complete=None):
        """Initialize the search frame."""
        super().__init__(parent, padding=PADDING["medium"], style="Card.TFrame")

        self.parent = parent
        self.api_client = api_client
        self.data_processor = data_processor
        self.on_search_complete = on_search_complete

        # Search parameters
        self.search_params = {
            "search_terms": "",
            "ad_type": "POLITICAL_AND_ISSUE_ADS",
            "ad_reached_countries": ["US"],
            "ad_active_status": "ACTIVE",
            "publisher_platforms": ["FACEBOOK", "INSTAGRAM"],
            "ad_delivery_date_min": (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d"),
            "ad_delivery_date_max": datetime.now().strftime("%Y-%m-%d")
        }

        self._create_widgets()
        self._layout_widgets()

    def _create_widgets(self):
        """Create the widgets for the search frame."""
        # Title
        self.title_label = ttk.Label(
            self,
            text="Search Parameters",
            font=FONTS["header"],
            foreground=COLORS["primary"],
            background=COLORS["card_bg"]
        )

        # Search terms
        self.search_terms_label = ttk.Label(
            self,
            text="Search Terms:",
            font=FONTS["normal"],
            background=COLORS["card_bg"]
        )
        self.search_terms_entry = ttk.Entry(
            self,
            width=50,
            font=FONTS["normal"]
        )
        self.search_terms_help = ttk.Label(
            self,
            text="Enter keywords to search for in ads",
            font=FONTS["small"],
            foreground=COLORS["light_text"],
            background=COLORS["card_bg"]
        )

        # Ad type
        self.ad_type_label = ttk.Label(
            self,
            text="Ad Type:",
            font=FONTS["normal"],
            background=COLORS["card_bg"]
        )
        self.ad_type_var = tk.StringVar(value=self.search_params["ad_type"])
        self.ad_type_combo = ttk.Combobox(
            self,
            textvariable=self.ad_type_var,
            values=[
                "ALL",
                "POLITICAL_AND_ISSUE_ADS",
                "HOUSING_ADS",
                "EMPLOYMENT_ADS",
                "FINANCIAL_PRODUCTS_AND_SERVICES_ADS"
            ],
            state="readonly",
            width=30,
            font=FONTS["normal"]
        )

        # Countries
        self.countries_label = ttk.Label(
            self,
            text="Countries:",
            font=FONTS["normal"],
            background=COLORS["card_bg"]
        )
        self.countries_entry = ttk.Entry(
            self,
            width=50,
            font=FONTS["normal"]
        )
        self.countries_entry.insert(0, "US")
        self.countries_help = ttk.Label(
            self,
            text="Enter country codes separated by commas (e.g., US,BR,DE)",
            font=FONTS["small"],
            foreground=COLORS["light_text"],
            background=COLORS["card_bg"]
        )

        # Date range
        self.date_label = ttk.Label(
            self,
            text="Date Range:",
            font=FONTS["normal"],
            background=COLORS["card_bg"]
        )

        self.date_frame = ttk.Frame(self, style="Card.TFrame")

        self.start_date_label = ttk.Label(
            self.date_frame,
            text="From:",
            font=FONTS["normal"],
            background=COLORS["card_bg"]
        )
        self.start_date_entry = ttk.Entry(
            self.date_frame,
            width=12,
            font=FONTS["normal"]
        )
        self.start_date_entry.insert(0, self.search_params["ad_delivery_date_min"])

        self.end_date_label = ttk.Label(
            self.date_frame,
            text="To:",
            font=FONTS["normal"],
            background=COLORS["card_bg"]
        )
        self.end_date_entry = ttk.Entry(
            self.date_frame,
            width=12,
            font=FONTS["normal"]
        )
        self.end_date_entry.insert(0, self.search_params["ad_delivery_date_max"])

        self.date_help = ttk.Label(
            self,
            text="Format: YYYY-MM-DD",
            font=FONTS["small"],
            foreground=COLORS["light_text"],
            background=COLORS["card_bg"]
        )

        # Platforms
        self.platforms_label = ttk.Label(
            self,
            text="Platforms:",
            font=FONTS["normal"],
            background=COLORS["card_bg"]
        )

        self.platforms_frame = ttk.Frame(self, style="Card.TFrame")

        # Platform checkboxes
        self.platform_vars = {
            "FACEBOOK": tk.BooleanVar(value=True),
            "INSTAGRAM": tk.BooleanVar(value=True),
            "AUDIENCE_NETWORK": tk.BooleanVar(value=False),
            "MESSENGER": tk.BooleanVar(value=False),
            "WHATSAPP": tk.BooleanVar(value=False)
        }

        self.platform_checkboxes = {}
        for idx, (platform_name, var) in enumerate(self.platform_vars.items()):
            self.platform_checkboxes[platform_name] = ttk.Checkbutton(
                self.platforms_frame,
                text=platform_name.capitalize(),
                variable=var,
                onvalue=True,
                offvalue=False,
                style="TCheckbutton"
            )

        # Active status
        self.status_label = ttk.Label(
            self,
            text="Ad Status:",
            font=FONTS["normal"],
            background=COLORS["card_bg"]
        )
        self.status_var = tk.StringVar(value=self.search_params["ad_active_status"])
        self.status_combo = ttk.Combobox(
            self,
            textvariable=self.status_var,
            values=["ACTIVE", "INACTIVE", "ALL"],
            state="readonly",
            width=15,
            font=FONTS["normal"]
        )

        # Search button
        self.search_button = ttk.Button(
            self,
            text="Search Ads",
            command=self.execute_search,
            style="Accent.TButton",
            padding=[PADDING["medium"], PADDING["small"]]
        )

        # Results count
        self.results_label = ttk.Label(
            self,
            text="",
            font=FONTS["normal"],
            background=COLORS["card_bg"]
        )

    def _layout_widgets(self):
        """Layout the widgets in the frame."""
        # Title
        self.title_label.grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, PADDING["large"]))

        # Search terms
        self.search_terms_label.grid(row=1, column=0, sticky="w", pady=(PADDING["small"], 0))
        self.search_terms_entry.grid(row=1, column=1, sticky="ew", pady=(PADDING["small"], 0))
        self.search_terms_help.grid(row=2, column=1, sticky="w", pady=(0, PADDING["medium"]))

        # Ad type
        self.ad_type_label.grid(row=3, column=0, sticky="w", pady=(PADDING["small"], 0))
        self.ad_type_combo.grid(row=3, column=1, sticky="w", pady=(PADDING["small"], PADDING["medium"]))

        # Countries
        self.countries_label.grid(row=4, column=0, sticky="w", pady=(PADDING["small"], 0))
        self.countries_entry.grid(row=4, column=1, sticky="ew", pady=(PADDING["small"], 0))
        self.countries_help.grid(row=5, column=1, sticky="w", pady=(0, PADDING["medium"]))

        # Date range
        self.date_label.grid(row=6, column=0, sticky="w", pady=(PADDING["small"], 0))
        self.date_frame.grid(row=6, column=1, sticky="w", pady=(PADDING["small"], 0))

        self.start_date_label.grid(row=0, column=0, sticky="w")
        self.start_date_entry.grid(row=0, column=1, sticky="w", padx=(PADDING["small"], PADDING["medium"]))
        self.end_date_label.grid(row=0, column=2, sticky="w")
        self.end_date_entry.grid(row=0, column=3, sticky="w", padx=(PADDING["small"], 0))

        self.date_help.grid(row=7, column=1, sticky="w", pady=(0, PADDING["medium"]))

        # Platforms
        self.platforms_label.grid(row=8, column=0, sticky="nw", pady=(PADDING["small"], 0))
        self.platforms_frame.grid(row=8, column=1, sticky="w", pady=(PADDING["small"], PADDING["medium"]))

        # Layout platform checkboxes in a grid (3 per row)
        for idx, (_, checkbox) in enumerate(self.platform_checkboxes.items()):
            row, col = divmod(idx, 3)
            checkbox.grid(row=row, column=col, sticky="w", padx=(0 if col == 0 else PADDING["medium"], 0))

        # Active status
        self.status_label.grid(row=9, column=0, sticky="w", pady=(PADDING["small"], 0))
        self.status_combo.grid(row=9, column=1, sticky="w", pady=(PADDING["small"], PADDING["medium"]))

        # Search button
        self.search_button.grid(row=10, column=0, columnspan=2, pady=PADDING["large"], sticky="ew", padx=PADDING["xlarge"])

        # Results count
        self.results_label.grid(row=11, column=0, columnspan=2, sticky="w", pady=PADDING["small"])

        # Configure grid
        self.columnconfigure(1, weight=1)

    def execute_search(self):
        """Execute the search with the current parameters."""
        try:
            # Update search parameters from UI
            self.search_params["search_terms"] = self.search_terms_entry.get()
            self.search_params["ad_type"] = self.ad_type_var.get()

            # Parse countries
            countries_text = self.countries_entry.get().strip()
            if countries_text:
                self.search_params["ad_reached_countries"] = [c.strip() for c in countries_text.split(",")]

            # Parse dates
            self.search_params["ad_delivery_date_min"] = self.start_date_entry.get()
            self.search_params["ad_delivery_date_max"] = self.end_date_entry.get()

            # Get selected platforms
            selected_platforms = [
                platform for platform, var in self.platform_vars.items()
                if var.get()
            ]
            if selected_platforms:
                self.search_params["publisher_platforms"] = selected_platforms

            # Get ad status
            self.search_params["ad_active_status"] = self.status_var.get()

            # Validate dates
            self._validate_dates()

            # Show searching message
            self.results_label.config(text="Searching... Please wait.")
            self.update_idletasks()

            # Execute search
            results = self.api_client.search_ads(self.search_params)

            # Process results
            processed_data = self.data_processor.process_ads_data(results)

            # Update results label
            self.results_label.config(
                text=f"Found {len(processed_data)} ads matching your criteria."
            )

            # Call the callback if provided
            if self.on_search_complete:
                self.on_search_complete(processed_data, self.search_params)

        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
        except Exception as e:
            messagebox.showerror("Search Error", f"An error occurred: {str(e)}")
            self.results_label.config(text="Search failed. See error message.")

    def _validate_dates(self):
        """Validate the date inputs."""
        date_format = "%Y-%m-%d"

        # Validate start date
        start_date_str = self.search_params["ad_delivery_date_min"]
        if start_date_str:
            try:
                datetime.strptime(start_date_str, date_format)
            except ValueError:
                raise ValueError("Start date must be in YYYY-MM-DD format")

        # Validate end date
        end_date_str = self.search_params["ad_delivery_date_max"]
        if end_date_str:
            try:
                datetime.strptime(end_date_str, date_format)
            except ValueError:
                raise ValueError("End date must be in YYYY-MM-DD format")

        # Validate date range
        if start_date_str and end_date_str:
            start_date = datetime.strptime(start_date_str, date_format)
            end_date = datetime.strptime(end_date_str, date_format)

            if start_date > end_date:
                raise ValueError("Start date cannot be after end date")
