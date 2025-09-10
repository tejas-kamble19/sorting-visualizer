"""
Main entry point for the Sorting Algorithm Visualizer
This file initializes the application and starts the GUI
"""

import tkinter as tk
import sys
import os

# Add the project root to Python path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from gui.main_window import MainWindow
from config.settings import APP_CONFIG

def main():
    """
    Main function that creates and runs the application
    """
    try:
        # Create the root Tkinter window
        root = tk.Tk()

        # Configure the main window properties
        root.title(APP_CONFIG['APP_NAME'])
        root.geometry(f"{APP_CONFIG['WINDOW_WIDTH']}x{APP_CONFIG['WINDOW_HEIGHT']}")
        root.resizable(True, True)
        root.minsize(APP_CONFIG['MIN_WINDOW_WIDTH'], APP_CONFIG['MIN_WINDOW_HEIGHT'])

        # Create the main application window
        app = MainWindow(root)

        # Start the GUI event loop
        root.mainloop()

    except Exception as e:
        print(f"Error starting application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
































#!/usr/bin/env python3
