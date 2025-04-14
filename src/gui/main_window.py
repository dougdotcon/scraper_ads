"""
Main window for the Meta Ads Library Scraper.
"""
import tkinter as tk
from tkinter import ttk, messagebox
import sys
from src.utils.config import UI_TITLE, UI_WIDTH, UI_HEIGHT, get_api_token
from src.api.auth import AuthManager
from src.api.client import APIClient
from src.data.processor import DataProcessor
from src.gui.search_frame import SearchFrame
from src.gui.config_frame import ConfigFrame
from src.gui.results_frame import ResultsFrame
from src.gui.styles import COLORS, FONTS, PADDING, NOTEBOOK_STYLES, TREEVIEW_STYLES, EFFECTS

class MainWindow:
    """Main window for the application."""

    def __init__(self, root):
        """Initialize the main window."""
        self.root = root
        self.root.title(UI_TITLE)
        self.root.geometry(f"{UI_WIDTH}x{UI_HEIGHT}")
        self.root.minsize(800, 600)

        # Set window icon if available
        try:
            import os
            if os.path.exists("assets/icons/app_icon.ico"):
                self.root.iconbitmap("assets/icons/app_icon.ico")
        except Exception:
            pass

        # Set up components
        self._setup_styles()
        self._setup_components()
        self._create_widgets()
        self._layout_widgets()

        # Check for API token on startup
        self._check_api_token()

    def _setup_styles(self):
        """Set up custom styles for ttk widgets."""
        style = ttk.Style()

        # Configure root window
        self.root.configure(background=COLORS["background"])

        # Configure TNotebook style
        style.configure(
            "TNotebook",
            background=COLORS["background"],
            tabposition=NOTEBOOK_STYLES["tabposition"],
            borderwidth=0
        )

        style.configure(
            "TNotebook.Tab",
            background=COLORS["background"],
            padding=[16, 8],
            font=FONTS["tab"],
            borderwidth=0
        )

        style.map(
            "TNotebook.Tab",
            background=[("selected", COLORS["primary"]), ("active", COLORS["hover"])],
            foreground=[("selected", COLORS["white"]), ("active", COLORS["primary"])]
        )

        # Configure button styles
        style.configure(
            "TButton",
            background=COLORS["background"],
            foreground=COLORS["text"],
            font=FONTS["button"],
            padding=[12, 6],
            borderwidth=1,
            relief="solid"
        )

        style.map(
            "TButton",
            background=[("active", COLORS["hover"])],
            foreground=[("active", COLORS["primary"])]
        )

        # Primary button style
        style.configure(
            "Accent.TButton",
            background=COLORS["primary"],
            foreground=COLORS["white"],
            font=FONTS["button"],
            padding=[12, 6],
            borderwidth=0,
            relief="flat"
        )

        style.map(
            "Accent.TButton",
            background=[("active", COLORS["primary_dark"])],
            foreground=[("active", COLORS["white"])]
        )

        # Secondary button style
        style.configure(
            "Secondary.TButton",
            background=COLORS["secondary"],
            foreground=COLORS["white"],
            font=FONTS["button"],
            padding=[12, 6],
            borderwidth=0,
            relief="flat"
        )

        style.map(
            "Secondary.TButton",
            background=[("active", "#4A5A7B")],
            foreground=[("active", COLORS["white"])]
        )

        # Accent button style
        style.configure(
            "Accent2.TButton",
            background=COLORS["accent"],
            foreground=COLORS["white"],
            font=FONTS["button"],
            padding=[12, 6],
            borderwidth=0,
            relief="flat"
        )

        style.map(
            "Accent2.TButton",
            background=[("active", COLORS["accent_dark"])],
            foreground=[("active", COLORS["white"])]
        )

        # Configure frame styles
        style.configure(
            "TFrame",
            background=COLORS["background"]
        )

        # Card frame style
        style.configure(
            "Card.TFrame",
            background=COLORS["card_bg"],
            relief="solid",
            borderwidth=1
        )

        # Raised card frame style
        style.configure(
            "CardRaised.TFrame",
            background=COLORS["card_bg"],
            relief="flat",
            borderwidth=0
        )

        # Configure labelframe styles
        style.configure(
            "TLabelframe",
            background=COLORS["background"],
            borderwidth=1,
            relief="solid"
        )

        style.configure(
            "TLabelframe.Label",
            background=COLORS["background"],
            foreground=COLORS["primary"],
            font=FONTS["section"]
        )

        # Card labelframe style
        style.configure(
            "Card.TLabelframe",
            background=COLORS["card_bg"],
            borderwidth=1,
            relief="solid"
        )

        style.configure(
            "Card.TLabelframe.Label",
            background=COLORS["card_bg"],
            foreground=COLORS["primary"],
            font=FONTS["section"]
        )

        # Configure label styles
        style.configure(
            "TLabel",
            background=COLORS["background"],
            foreground=COLORS["text"],
            font=FONTS["normal"]
        )

        # Configure entry styles
        style.configure(
            "TEntry",
            fieldbackground=COLORS["white"],
            foreground=COLORS["text"],
            font=FONTS["normal"],
            borderwidth=1,
            relief="solid"
        )

        # Configure combobox styles
        style.configure(
            "TCombobox",
            fieldbackground=COLORS["white"],
            background=COLORS["white"],
            foreground=COLORS["text"],
            arrowcolor=COLORS["primary"],
            font=FONTS["normal"]
        )

        style.map(
            "TCombobox",
            fieldbackground=[("readonly", COLORS["white"])],
            selectbackground=[("readonly", COLORS["primary"])],
            selectforeground=[("readonly", COLORS["white"])]
        )

        # Configure treeview styles
        style.configure(
            "Treeview",
            background=TREEVIEW_STYLES["background"],
            fieldbackground=TREEVIEW_STYLES["fieldbackground"],
            foreground=TREEVIEW_STYLES["foreground"],
            font=TREEVIEW_STYLES["font"],
            rowheight=TREEVIEW_STYLES["rowheight"],
            borderwidth=TREEVIEW_STYLES["borderwidth"],
            relief=TREEVIEW_STYLES["relief"]
        )

        style.configure(
            "Treeview.Heading",
            background=COLORS["primary"],
            foreground=COLORS["white"],
            font=FONTS["button"],
            relief="flat",
            borderwidth=0
        )

        style.map(
            "Treeview",
            background=[("selected", COLORS["primary"])],
            foreground=[("selected", COLORS["white"])]
        )

    def _setup_components(self):
        """Set up the application components."""
        # Create auth manager
        self.auth_manager = AuthManager(get_api_token())

        # Create API client
        self.api_client = APIClient(self.auth_manager)

        # Create data processor
        self.data_processor = DataProcessor()

    def _create_widgets(self):
        """Create the widgets for the main window."""
        # Create main container with scrollbars
        self.main_canvas = tk.Canvas(self.root, background=COLORS["background"], highlightthickness=0)
        self.main_scrollbar_y = ttk.Scrollbar(self.root, orient="vertical", command=self.main_canvas.yview)
        self.main_scrollbar_x = ttk.Scrollbar(self.root, orient="horizontal", command=self.main_canvas.xview)
        self.main_canvas.configure(yscrollcommand=self.main_scrollbar_y.set, xscrollcommand=self.main_scrollbar_x.set)

        # Set scrollbar style
        style = ttk.Style()
        style.configure("Vertical.TScrollbar", gripcount=0, background=COLORS["background"], darkcolor=COLORS["primary"], lightcolor=COLORS["primary"], troughcolor=COLORS["background"], bordercolor=COLORS["border"], arrowcolor=COLORS["primary"])
        style.configure("Horizontal.TScrollbar", gripcount=0, background=COLORS["background"], darkcolor=COLORS["primary"], lightcolor=COLORS["primary"], troughcolor=COLORS["background"], bordercolor=COLORS["border"], arrowcolor=COLORS["primary"])
        self.main_scrollbar_y.configure(style="Vertical.TScrollbar")
        self.main_scrollbar_x.configure(style="Horizontal.TScrollbar")

        # Create a frame inside the canvas for all content
        self.main_frame = ttk.Frame(self.main_canvas, style="TFrame")
        self.canvas_frame_id = self.main_canvas.create_window((0, 0), window=self.main_frame, anchor="nw")

        # Create notebook (tabbed interface)
        self.notebook = ttk.Notebook(self.main_frame)

        # Create frames for each tab
        self.search_frame = SearchFrame(
            self.notebook,
            self.api_client,
            self.data_processor,
            self._on_search_complete
        )

        self.config_frame = ConfigFrame(
            self.notebook,
            self.auth_manager
        )

        self.results_frame = ResultsFrame(self.main_frame)

        # Add frames to notebook
        self.notebook.add(self.search_frame, text="Search")
        self.notebook.add(self.config_frame, text="Configuration")

        # Configure canvas scrolling
        self.main_frame.bind("<Configure>", self._on_frame_configure)
        self.main_canvas.bind("<Configure>", self._on_canvas_configure)

        # Status bar
        self.status_bar = ttk.Frame(self.root, relief=tk.SUNKEN, padding=(2, 2))
        self.status_label = ttk.Label(
            self.status_bar,
            text="Ready",
            anchor=tk.W
        )

    def _layout_widgets(self):
        """Layout the widgets in the window."""
        # Configure root grid
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=0)  # Y scrollbar
        self.root.rowconfigure(0, weight=1)  # Canvas
        self.root.rowconfigure(1, weight=0)  # X scrollbar
        self.root.rowconfigure(2, weight=0)  # Status bar

        # Place scrollbars and canvas
        self.main_canvas.grid(row=0, column=0, sticky="nsew")
        self.main_scrollbar_y.grid(row=0, column=1, sticky="ns")
        self.main_scrollbar_x.grid(row=1, column=0, sticky="ew")

        # Configure main_frame grid
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(0, weight=0)  # Notebook
        self.main_frame.rowconfigure(1, weight=1)  # Results

        # Place widgets in main_frame
        self.notebook.grid(row=0, column=0, sticky="ew", padx=PADDING["medium"], pady=PADDING["medium"])
        self.results_frame.grid(row=1, column=0, sticky="nsew", padx=PADDING["medium"], pady=PADDING["small"])

        # Status bar
        self.status_bar.grid(row=2, column=0, columnspan=2, sticky="ew")
        self.status_label.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=PADDING["small"])

        # Configure status bar
        self.status_bar.columnconfigure(0, weight=1)

    def _check_api_token(self):
        """Check if an API token is available on startup."""
        token = get_api_token()
        if not token:
            # Switch to config tab if no token is available
            self.notebook.select(1)  # Index 1 is the config tab
            self.status_label.config(text="Please configure your API token")
        else:
            self.auth_manager.set_token(token)
            self.status_label.config(text="API token loaded from configuration")

    def _on_search_complete(self, data, search_params):
        """Handle search completion."""
        # Update results frame
        self.results_frame.update_results(data, search_params)

        # Update status
        self.status_label.config(text=f"Found {len(data)} ads matching your criteria")

    def _on_frame_configure(self, event):
        """Update the scrollregion when the frame size changes."""
        self.main_canvas.configure(scrollregion=self.main_canvas.bbox("all"))

    def _on_canvas_configure(self, event):
        """Resize the frame inside the canvas when the canvas size changes."""
        # Update the width of the frame to fill the canvas
        self.main_canvas.itemconfig(self.canvas_frame_id, width=event.width)

    def run(self):
        """Run the main event loop."""
        # Set initial size and position
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - UI_WIDTH) // 2
        y = (screen_height - UI_HEIGHT) // 2
        self.root.geometry(f"{UI_WIDTH}x{UI_HEIGHT}+{x}+{y}")

        # Enable mouse wheel scrolling
        self.root.bind("<MouseWheel>", lambda event: self.main_canvas.yview_scroll(-1 * (event.delta // 120), "units"))
        self.root.bind("<Shift-MouseWheel>", lambda event: self.main_canvas.xview_scroll(-1 * (event.delta // 120), "units"))

        # For Linux/Unix systems
        self.root.bind("<Button-4>", lambda event: self.main_canvas.yview_scroll(-1, "units"))
        self.root.bind("<Button-5>", lambda event: self.main_canvas.yview_scroll(1, "units"))
        self.root.bind("<Shift-Button-4>", lambda event: self.main_canvas.xview_scroll(-1, "units"))
        self.root.bind("<Shift-Button-5>", lambda event: self.main_canvas.xview_scroll(1, "units"))

        self.root.mainloop()
