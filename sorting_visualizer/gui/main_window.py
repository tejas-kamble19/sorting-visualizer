"""
Main application window that contains all GUI components
"""

import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time

from .visualization_canvas import VisualizationCanvas
from .control_panel import ControlPanel
from algorithms import get_algorithm_by_name, get_available_algorithms
from utils.data_generator import DataGenerator
from utils.complexity_analyzer import ComplexityAnalyzer
from config.settings import APP_CONFIG, COLORS

class MainWindow:
    def __init__(self, root):
        """
        Initialize the main window with all components

        Args:
            root: The main Tkinter window object
        """
        self.root = root
        self.setup_window()
        self.create_widgets()
        self.layout_widgets()
        self.bind_events()

        # Initialize components
        self.data_generator = DataGenerator()
        self.complexity_analyzer = ComplexityAnalyzer()

        # Application state
        self.current_algorithm = None
        self.is_sorting = False
        self.is_paused = False
        self.sorting_thread = None
        self.array_data = []
        self.original_array = []

        # Performance tracking
        self.start_time = 0
        self.comparisons = 0
        self.swaps = 0

        # Initialize with default algorithm info
        self.control_panel.update_algorithm_info('bubble_sort')

        # Generate initial data
        self.generate_new_array()

    def setup_window(self):
        """Configure the main window"""
        self.root.configure(bg=COLORS['background'])

        # Configure grid weights for resizing
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

    def create_widgets(self):
        """Create all GUI widgets"""
        # Main container
        self.main_frame = tk.Frame(self.root, bg=COLORS['background'])

        # Title section
        self.title_frame = tk.Frame(self.main_frame, bg=COLORS['background'])

        self.title_label = tk.Label(
            self.title_frame,
            text="Sorting Algorithm Visualizer",
            font=('Arial', 24, 'bold'),
            fg=COLORS['text'],
            bg=COLORS['background']
        )

        self.subtitle_label = tk.Label(
            self.title_frame,
            text="Interactive visualization showing algorithmic thinking + UI skills + complexity analysis",
            font=('Arial', 12),
            fg=COLORS['text_secondary'],
            bg=COLORS['background']
        )

        # Main content area
        self.content_frame = tk.Frame(self.main_frame, bg=COLORS['background'])

        # Visualization canvas
        self.canvas = VisualizationCanvas(self.content_frame)

        # Control panel
        self.control_panel = ControlPanel(self.content_frame, self)

        # Status bar
        self.status_frame = tk.Frame(self.main_frame, bg=COLORS['surface'])

        self.status_var = tk.StringVar()
        self.status_var.set("Ready - Generate an array and select an algorithm to begin")

        self.status_bar = tk.Label(
            self.status_frame,
            textvariable=self.status_var,
            relief=tk.SUNKEN,
            anchor=tk.W,
            bg=COLORS['surface'],
            fg=COLORS['text'],
            font=('Arial', 10)
        )

    def layout_widgets(self):
        """Arrange all widgets using grid layout"""
        # Main frame fills the entire window
        self.main_frame.grid(row=0, column=0, sticky='nsew')
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(2, weight=1)

        # Title section
        self.title_frame.grid(row=0, column=0, sticky='ew', padx=20, pady=10)
        self.title_label.pack()
        self.subtitle_label.pack(pady=(5, 0))

        # Content area
        self.content_frame.grid(row=2, column=0, sticky='nsew', padx=20, pady=10)
        self.content_frame.columnconfigure(0, weight=3)  # Canvas gets more space
        self.content_frame.columnconfigure(1, weight=1)  # Control panel
        self.content_frame.rowconfigure(0, weight=1)

        # Canvas and control panel
        self.canvas.grid(row=0, column=0, sticky='nsew', padx=(0, 10))
        self.control_panel.grid(row=0, column=1, sticky='nsew')

        # Status bar
        self.status_frame.grid(row=3, column=0, sticky='ew')
        self.status_bar.pack(fill='x', padx=5, pady=2)

    def bind_events(self):
        """Set up event handlers"""
        self.root.bind('<KeyPress>', self.on_key_press)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Make window focusable for keyboard events
        self.root.focus_set()

    def on_key_press(self, event):
        """Handle keyboard shortcuts"""
        key = event.keysym.lower()

        if key == 'space':
            self.toggle_sorting()
        elif key == 'r':
            self.reset_array()
        elif key == 'g':
            self.generate_new_array()
        elif key == 'escape' and self.is_sorting:
            self.stop_sorting()

    def generate_new_array(self):
        """Generate a new random array for sorting"""
        if self.is_sorting:
            return

        size = self.control_panel.get_array_size()
        self.array_data = self.data_generator.generate_random_array(size)
        self.original_array = self.array_data.copy()
        self.canvas.draw_array(self.array_data)

        # Reset statistics
        self.comparisons = 0
        self.swaps = 0
        self.control_panel.update_statistics(0, 0, 0)

        self.update_status("New array generated - Ready to sort")

    def load_array_from_file(self, filename):
        """Load array from file"""
        if self.is_sorting:
            return

        try:
            self.array_data = self.data_generator.load_from_file(filename)
            self.original_array = self.array_data.copy()
            self.canvas.draw_array(self.array_data)

            # Reset statistics
            self.comparisons = 0
            self.swaps = 0
            self.control_panel.update_statistics(0, 0, 0)

            self.update_status(f"Array loaded from {filename} - Ready to sort")
        except Exception as e:
            messagebox.showerror("Error", f"Could not load file: {str(e)}")

    def start_sorting(self):
        """Start the sorting animation"""
        if self.is_sorting or not self.array_data:
            return

        algorithm_name = self.control_panel.get_selected_algorithm()

        try:
            self.current_algorithm = get_algorithm_by_name(
                algorithm_name,
                self.array_data.copy(),
                self.on_algorithm_step
            )
        except Exception as e:
            messagebox.showerror("Error", f"Could not create algorithm: {str(e)}")
            return

        self.is_sorting = True
        self.is_paused = False
        self.control_panel.set_sorting_state(True)

        # Reset statistics
        self.comparisons = 0
        self.swaps = 0
        self.start_time = time.time()

        # Start sorting in a separate thread to keep GUI responsive
        self.sorting_thread = threading.Thread(
            target=self.run_sorting_algorithm,
            daemon=True
        )
        self.sorting_thread.start()

        algorithm_display_name = self.control_panel.algorithm_combo.get()
        self.update_status(f"Sorting with {algorithm_display_name}...")

    def pause_sorting(self):
        """Pause the current sorting operation"""
        if not self.is_sorting:
            return

        self.is_paused = not self.is_paused
        if self.current_algorithm:
            if self.is_paused:
                self.current_algorithm.stop()
                self.update_status("Sorting paused")
                self.control_panel.start_btn.config(text="Resume")
            else:
                self.current_algorithm.is_running = True
                self.update_status("Sorting resumed")
                self.control_panel.start_btn.config(text="Pause")

    def stop_sorting(self):
        """Stop the current sorting operation"""
        if not self.is_sorting:
            return

        if self.current_algorithm:
            self.current_algorithm.stop()

        self.is_sorting = False
        self.is_paused = False
        self.control_panel.set_sorting_state(False)
        self.update_status("Sorting stopped")

    def reset_array(self):
        """Reset array to original unsorted state"""
        if self.is_sorting:
            self.stop_sorting()

        if self.original_array:
            self.array_data = self.original_array.copy()
            self.canvas.draw_array(self.array_data)

            # Reset statistics
            self.comparisons = 0
            self.swaps = 0
            self.control_panel.update_statistics(0, 0, 0)

            self.update_status("Array reset to original state")

    def toggle_sorting(self):
        """Toggle between start and pause"""
        if not self.is_sorting:
            self.start_sorting()
        else:
            self.pause_sorting()

    def run_sorting_algorithm(self):
        """Run the sorting algorithm (called in separate thread)"""
        try:
            self.current_algorithm.sort()

            # Schedule completion handling on main thread
            self.root.after(0, self.on_sorting_complete)

        except Exception as e:
            # Schedule error handling on main thread
            self.root.after(0, lambda: self.on_sorting_error(str(e)))

    def on_algorithm_step(self, operation, indices, array_state):
        """
        Called by the algorithm for each step
        This updates the visualization
        """
        if not self.is_sorting or self.is_paused:
            return

        # Update statistics
        if operation == 'compare':
            self.comparisons += 1
        elif operation == 'swap':
            self.swaps += 1

        # Update display (must be called from main thread)
        self.root.after(0, lambda: self._update_display(operation, indices, array_state))

        # Control animation speed
        speed = self.control_panel.get_animation_speed()
        delay = max(10, 200 - (speed * 18)) / 1000.0  # Convert to seconds
        time.sleep(delay)

    def _update_display(self, operation, indices, array_state):
        """Update display elements (called from main thread)"""
        # Update canvas
        self.canvas.update_visualization(operation, indices, array_state)

        # Update statistics
        elapsed_time = time.time() - self.start_time if self.start_time else 0
        self.control_panel.update_statistics(self.comparisons, self.swaps, elapsed_time)

    def on_sorting_complete(self):
        """Called when sorting is finished"""
        self.is_sorting = False
        self.is_paused = False
        self.control_panel.set_sorting_state(False)
        self.canvas.mark_all_sorted()

        # Calculate final statistics
        elapsed_time = time.time() - self.start_time if self.start_time else 0
        self.control_panel.update_statistics(self.comparisons, self.swaps, elapsed_time)

        # Show completion message
        algorithm_name = self.control_panel.algorithm_combo.get()
        message = f"""{algorithm_name} completed!

Statistics:
• Comparisons: {self.comparisons:,}
• Swaps: {self.swaps:,}  
• Time: {elapsed_time:.3f} seconds
• Array Size: {len(self.array_data)} elements

Efficiency:
• {self.comparisons/len(self.array_data):.1f} comparisons per element
• {self.swaps/len(self.array_data):.1f} swaps per element"""

        self.update_status(f"{algorithm_name} completed successfully!")
        messagebox.showinfo("Sorting Complete", message)

    def on_sorting_error(self, error_message):
        """Called when an error occurs during sorting"""
        self.is_sorting = False
        self.is_paused = False
        self.control_panel.set_sorting_state(False)
        self.update_status("Error occurred during sorting")
        messagebox.showerror("Sorting Error", f"An error occurred: {error_message}")

    def update_status(self, message):
        """Update the status bar with a new message"""
        self.status_var.set(message)
        self.root.update_idletasks()

    def on_closing(self):
        """Handle application closing"""
        if self.is_sorting:
            if messagebox.askokcancel("Quit", "Sorting is in progress. Do you want to quit?"):
                if self.current_algorithm:
                    self.current_algorithm.stop()
                self.root.destroy()
        else:
            self.root.destroy()
