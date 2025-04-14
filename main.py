"""
Meta Ads Library Scraper

A tool to extract data from the Meta Ads Library API with a graphical interface.
"""
import tkinter as tk
import sys
import os
from src.gui.main_window import MainWindow

def main():
    """Main entry point for the application."""
    # Create the root window
    root = tk.Tk()
    
    # Set icon if available
    icon_path = os.path.join("assets", "icons", "app_icon.ico")
    if os.path.exists(icon_path):
        root.iconbitmap(icon_path)
    
    # Create and run the main window
    app = MainWindow(root)
    app.run()

if __name__ == "__main__":
    main()
