"""
Styles for the GUI components.
"""

# Colors - Modern palette
COLORS = {
    "primary": "#1877F2",       # Bright blue (Meta blue)
    "primary_dark": "#0A66C2",  # Darker blue for hover states
    "secondary": "#5B6B8C",     # Slate blue
    "accent": "#00C6AE",        # Teal accent
    "accent_dark": "#00A896",   # Darker teal for hover states
    "background": "#F8F9FA",    # Light gray background
    "card_bg": "#FFFFFF",       # White for cards
    "text": "#1C1E21",          # Almost black for main text
    "light_text": "#65676B",    # Gray for secondary text
    "white": "#FFFFFF",         # Pure white
    "error": "#E41E3F",         # Red for errors
    "warning": "#F7B928",       # Yellow for warnings
    "success": "#00C48C",       # Green for success messages
    "border": "#E4E6EB",        # Light gray for borders
    "hover": "#E7F3FF",         # Light blue for hover states
    "disabled": "#E9EBEE",      # Gray for disabled elements
    "shadow": "rgba(0, 0, 0, 0.1)" # Shadow color
}

# Font configurations
FONTS = {
    "header": ("Segoe UI", 20, "bold"),
    "subheader": ("Segoe UI", 16, "bold"),
    "section": ("Segoe UI", 14, "bold"),
    "normal": ("Segoe UI", 11),
    "small": ("Segoe UI", 10),
    "tiny": ("Segoe UI", 9),
    "button": ("Segoe UI", 11, "bold"),
    "tab": ("Segoe UI", 11, "bold")
}

# Padding and spacing
PADDING = {
    "tiny": 3,
    "small": 6,
    "medium": 12,
    "large": 18,
    "xlarge": 24,
    "xxlarge": 32
}

# Button styles
BUTTON_STYLES = {
    "primary": {
        "bg": COLORS["primary"],
        "fg": COLORS["white"],
        "activebackground": COLORS["primary_dark"],
        "activeforeground": COLORS["white"],
        "font": FONTS["button"],
        "borderwidth": 0,
        "padx": 16,
        "pady": 8,
        "cursor": "hand2",
        "relief": "flat",
        "highlightthickness": 0
    },
    "secondary": {
        "bg": COLORS["secondary"],
        "fg": COLORS["white"],
        "activebackground": "#4A5A7B",  # Darker shade of secondary
        "activeforeground": COLORS["white"],
        "font": FONTS["button"],
        "borderwidth": 0,
        "padx": 16,
        "pady": 8,
        "cursor": "hand2",
        "relief": "flat",
        "highlightthickness": 0
    },
    "accent": {
        "bg": COLORS["accent"],
        "fg": COLORS["white"],
        "activebackground": COLORS["accent_dark"],
        "activeforeground": COLORS["white"],
        "font": FONTS["button"],
        "borderwidth": 0,
        "padx": 16,
        "pady": 8,
        "cursor": "hand2",
        "relief": "flat",
        "highlightthickness": 0
    },
    "outline": {
        "bg": COLORS["white"],
        "fg": COLORS["primary"],
        "activebackground": COLORS["hover"],
        "activeforeground": COLORS["primary_dark"],
        "font": FONTS["button"],
        "borderwidth": 1,
        "relief": "solid",
        "padx": 16,
        "pady": 8,
        "cursor": "hand2",
        "highlightthickness": 0,
        "highlightbackground": COLORS["primary"]
    }
}

# Entry field styles
ENTRY_STYLES = {
    "bg": COLORS["white"],
    "fg": COLORS["text"],
    "insertbackground": COLORS["text"],
    "font": FONTS["normal"],
    "borderwidth": 1,
    "relief": "solid",
    "highlightthickness": 1,
    "highlightcolor": COLORS["primary"],
    "highlightbackground": COLORS["border"],
    "selectbackground": COLORS["primary"],
    "selectforeground": COLORS["white"],
    "padx": 8,
    "pady": 6
}

# Frame styles
FRAME_STYLES = {
    "main": {
        "bg": COLORS["background"],
        "padx": PADDING["medium"],
        "pady": PADDING["medium"]
    },
    "card": {
        "bg": COLORS["card_bg"],
        "padx": PADDING["medium"],
        "pady": PADDING["medium"],
        "borderwidth": 1,
        "relief": "solid",
        "highlightthickness": 0
    },
    "card_raised": {
        "bg": COLORS["card_bg"],
        "padx": PADDING["medium"],
        "pady": PADDING["medium"],
        "borderwidth": 0,
        "relief": "flat",
        "highlightthickness": 0
    },
    "section": {
        "bg": COLORS["background"],
        "padx": PADDING["medium"],
        "pady": PADDING["medium"],
        "borderwidth": 0,
        "relief": "flat"
    }
}

# Label styles
LABEL_STYLES = {
    "header": {
        "bg": COLORS["background"],
        "fg": COLORS["primary"],
        "font": FONTS["header"]
    },
    "subheader": {
        "bg": COLORS["background"],
        "fg": COLORS["text"],
        "font": FONTS["subheader"]
    },
    "section": {
        "bg": COLORS["background"],
        "fg": COLORS["secondary"],
        "font": FONTS["section"]
    },
    "normal": {
        "bg": COLORS["background"],
        "fg": COLORS["text"],
        "font": FONTS["normal"]
    },
    "normal_card": {
        "bg": COLORS["card_bg"],
        "fg": COLORS["text"],
        "font": FONTS["normal"]
    },
    "small": {
        "bg": COLORS["background"],
        "fg": COLORS["light_text"],
        "font": FONTS["small"]
    },
    "small_card": {
        "bg": COLORS["card_bg"],
        "fg": COLORS["light_text"],
        "font": FONTS["small"]
    },
    "accent": {
        "bg": COLORS["background"],
        "fg": COLORS["accent"],
        "font": FONTS["normal"]
    },
    "error": {
        "bg": COLORS["background"],
        "fg": COLORS["error"],
        "font": FONTS["small"]
    },
    "success": {
        "bg": COLORS["background"],
        "fg": COLORS["success"],
        "font": FONTS["small"]
    }
}

# Notebook (tabbed interface) styles
NOTEBOOK_STYLES = {
    "tabposition": "n",
    "padding": 10,
    "tabmargins": 2,
    "background": COLORS["background"],
    "borderwidth": 0
}

# Treeview styles
TREEVIEW_STYLES = {
    "background": COLORS["white"],
    "fieldbackground": COLORS["white"],
    "foreground": COLORS["text"],
    "font": FONTS["normal"],
    "rowheight": 30,
    "borderwidth": 0,
    "relief": "flat"
}

# Custom effects
EFFECTS = {
    "shadow": "2px 2px 5px " + COLORS["shadow"],
    "transition": "0.3s"
}
