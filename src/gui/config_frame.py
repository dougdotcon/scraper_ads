"""
Configuration frame for the Meta Ads Library Scraper.
"""
import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser
from src.utils.config import get_api_token, save_api_token
from src.api.auth import AuthManager
from src.gui.styles import COLORS, FONTS, PADDING, BUTTON_STYLES, ENTRY_STYLES, FRAME_STYLES, LABEL_STYLES

class ConfigFrame(ttk.Frame):
    """Frame for API configuration settings."""

    def __init__(self, parent, auth_manager=None):
        """Initialize the configuration frame."""
        super().__init__(parent, padding=PADDING["medium"], style="Card.TFrame")

        self.parent = parent
        self.auth_manager = auth_manager or AuthManager()

        self._create_widgets()
        self._layout_widgets()

        # Load saved token if available
        saved_token = get_api_token()
        if saved_token:
            self.token_entry.insert(0, saved_token)
            self.auth_manager.set_token(saved_token)

    def _create_widgets(self):
        """Create the widgets for the configuration frame."""
        # Title
        self.title_label = ttk.Label(
            self,
            text="API Configuration",
            font=FONTS["header"],
            foreground=COLORS["primary"],
            background=COLORS["card_bg"]
        )

        # API Token section
        self.token_frame = ttk.LabelFrame(
            self,
            text="Meta Ads Library API Token",
            padding=PADDING["medium"],
            style="Card.TLabelframe"
        )

        self.token_label = ttk.Label(
            self.token_frame,
            text="Access Token:",
            font=FONTS["normal"],
            background=COLORS["card_bg"]
        )

        self.token_entry = ttk.Entry(
            self.token_frame,
            width=50,
            font=FONTS["normal"],
            show="•"  # Mask the token for security
        )

        self.show_token_var = tk.BooleanVar(value=False)
        self.show_token_check = ttk.Checkbutton(
            self.token_frame,
            text="Show token",
            variable=self.show_token_var,
            command=self._toggle_token_visibility
        )

        self.token_help = ttk.Label(
            self.token_frame,
            text="Enter your Meta Ads Library API access token",
            font=FONTS["small"],
            foreground=COLORS["light_text"],
            background=COLORS["card_bg"]
        )

        self.save_token_button = ttk.Button(
            self.token_frame,
            text="Save Token",
            command=self._save_token,
            style="Accent.TButton",
            padding=[PADDING["medium"], PADDING["small"]]
        )

        self.validate_token_button = ttk.Button(
            self.token_frame,
            text="Validate Token",
            command=self._validate_token,
            style="Secondary.TButton",
            padding=[PADDING["medium"], PADDING["small"]]
        )

        # Help section
        self.help_frame = ttk.LabelFrame(
            self,
            text="Help & Resources",
            padding=PADDING["medium"],
            style="Card.TLabelframe"
        )

        self.help_text = ttk.Label(
            self.help_frame,
            text="To use the Meta Ads Library API, you need to create a developer account and obtain an access token.",
            font=FONTS["normal"],
            wraplength=500,
            background=COLORS["card_bg"]
        )

        self.help_steps = ttk.Label(
            self.help_frame,
            text="1. Create a Meta for Developers account\n"
                 "2. Create a new app\n"
                 "3. Generate an access token with ads_read permission\n"
                 "4. Enter the token above and click 'Save Token'",
            font=FONTS["normal"],
            background=COLORS["card_bg"]
        )

        self.docs_button = ttk.Button(
            self.help_frame,
            text="Open API Documentation",
            command=lambda: webbrowser.open("https://developers.facebook.com/docs/marketing-api/reference/ads-archive/"),
            style="Accent2.TButton",
            padding=[PADDING["medium"], PADDING["small"]]
        )

        # Advanced settings section
        self.advanced_frame = ttk.LabelFrame(
            self,
            text="Advanced Settings",
            padding=PADDING["medium"],
            style="Card.TLabelframe"
        )

        self.api_version_label = ttk.Label(
            self.advanced_frame,
            text="API Version:",
            font=FONTS["normal"],
            background=COLORS["card_bg"]
        )

        self.api_version_var = tk.StringVar(value="v19.0")
        self.api_version_combo = ttk.Combobox(
            self.advanced_frame,
            textvariable=self.api_version_var,
            values=["v19.0", "v18.0", "v17.0"],
            state="readonly",
            width=10,
            font=FONTS["normal"]
        )

        self.rate_limit_label = ttk.Label(
            self.advanced_frame,
            text="Rate Limit Handling:",
            font=FONTS["normal"],
            background=COLORS["card_bg"]
        )

        self.rate_limit_var = tk.BooleanVar(value=True)
        self.rate_limit_check = ttk.Checkbutton(
            self.advanced_frame,
            text="Automatically handle rate limits",
            variable=self.rate_limit_var
        )

        self.max_results_label = ttk.Label(
            self.advanced_frame,
            text="Max Results:",
            font=FONTS["normal"],
            background=COLORS["card_bg"]
        )

        self.max_results_var = tk.StringVar(value="1000")
        self.max_results_entry = ttk.Entry(
            self.advanced_frame,
            textvariable=self.max_results_var,
            width=10,
            font=FONTS["normal"]
        )

        # Status indicator
        self.status_frame = ttk.Frame(self, style="Card.TFrame")

        self.status_label = ttk.Label(
            self.status_frame,
            text="Token Status:",
            font=FONTS["normal"],
            background=COLORS["card_bg"]
        )

        self.status_indicator = ttk.Label(
            self.status_frame,
            text="Not Validated",
            font=FONTS["normal"],
            foreground=COLORS["secondary"],
            background=COLORS["card_bg"]
        )

    def _layout_widgets(self):
        """Layout the widgets in the frame."""
        # Title
        self.title_label.grid(row=0, column=0, sticky="w", pady=(0, PADDING["large"]))

        # Token section
        self.token_frame.grid(row=1, column=0, sticky="ew", pady=PADDING["medium"])

        self.token_label.grid(row=0, column=0, sticky="w", pady=PADDING["small"])
        self.token_entry.grid(row=0, column=1, sticky="ew", pady=PADDING["small"])
        self.show_token_check.grid(row=0, column=2, sticky="w", padx=PADDING["small"], pady=PADDING["small"])
        self.token_help.grid(row=1, column=1, sticky="w", pady=(0, PADDING["small"]))

        token_buttons_frame = ttk.Frame(self.token_frame, style="Card.TFrame")
        token_buttons_frame.grid(row=2, column=1, sticky="w", pady=PADDING["medium"])

        self.save_token_button.grid(row=0, column=0, padx=(0, PADDING["small"]))
        self.validate_token_button.grid(row=0, column=1)

        # Help section
        self.help_frame.grid(row=2, column=0, sticky="ew", pady=PADDING["medium"])

        self.help_text.grid(row=0, column=0, sticky="w", pady=PADDING["small"])
        self.help_steps.grid(row=1, column=0, sticky="w", pady=PADDING["medium"])
        self.docs_button.grid(row=2, column=0, sticky="w", pady=PADDING["small"])

        # Advanced settings section
        self.advanced_frame.grid(row=3, column=0, sticky="ew", pady=PADDING["medium"])

        self.api_version_label.grid(row=0, column=0, sticky="w", pady=PADDING["small"])
        self.api_version_combo.grid(row=0, column=1, sticky="w", pady=PADDING["small"])

        self.rate_limit_label.grid(row=1, column=0, sticky="w", pady=PADDING["small"])
        self.rate_limit_check.grid(row=1, column=1, sticky="w", pady=PADDING["small"])

        self.max_results_label.grid(row=2, column=0, sticky="w", pady=PADDING["small"])
        self.max_results_entry.grid(row=2, column=1, sticky="w", pady=PADDING["small"])

        # Status indicator
        self.status_frame.grid(row=4, column=0, sticky="ew", pady=PADDING["large"])

        self.status_label.grid(row=0, column=0, sticky="w")
        self.status_indicator.grid(row=0, column=1, sticky="w", padx=PADDING["small"])

        # Configure grid
        self.columnconfigure(0, weight=1)
        self.token_frame.columnconfigure(1, weight=1)

    def _toggle_token_visibility(self):
        """Toggle the visibility of the token."""
        if self.show_token_var.get():
            self.token_entry.config(show="")
        else:
            self.token_entry.config(show="•")

    def _save_token(self):
        """Save the API token."""
        token = self.token_entry.get().strip()

        if not token:
            messagebox.showerror("Error", "Please enter an API token")
            return

        try:
            # Save token to config
            save_api_token(token)

            # Update auth manager
            self.auth_manager.set_token(token)

            messagebox.showinfo("Success", "API token saved successfully")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to save token: {str(e)}")

    def _validate_token(self):
        """Validate the API token."""
        token = self.token_entry.get().strip()

        if not token:
            messagebox.showerror("Error", "Please enter an API token")
            return

        # Update the status indicator
        self.status_indicator.config(
            text="Validating...",
            foreground=COLORS["secondary"]
        )
        self.update_idletasks()

        # Set the token in the auth manager
        self.auth_manager.set_token(token)

        # Validate the token
        is_valid = self.auth_manager.validate_token()

        if is_valid:
            self.status_indicator.config(
                text="Valid",
                foreground=COLORS["success"]
            )
            messagebox.showinfo("Success", "API token is valid")
        else:
            self.status_indicator.config(
                text="Invalid",
                foreground=COLORS["error"]
            )
            messagebox.showerror("Error", "API token is invalid or has expired")

    def get_token(self):
        """Get the current API token."""
        return self.token_entry.get().strip()
