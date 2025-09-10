"""
Visualization canvas that draws the sorting animation using matplotlib embedded in tkinter
"""

import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
from config.settings import COLORS, VISUAL_CONFIG
from utils.color_manager import ColorManager

class VisualizationCanvas(tk.Frame):
    def __init__(self, parent, **kwargs):
        """
        Initialize the visualization canvas

        Args:
            parent: Parent widget
            **kwargs: Frame configuration options
        """
        super().__init__(parent, **kwargs)

        self.color_manager = ColorManager()
        self.array_data = []
        self.bar_colors = []
        self.bars = []

        # Create matplotlib figure
        self.figure = Figure(figsize=(10, 6), dpi=100)
        self.figure.patch.set_facecolor(COLORS['background'])

        self.ax = self.figure.add_subplot(111)
        self.ax.set_facecolor(COLORS['background'])

        # Create canvas widget
        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # Initialize empty plot
        self.setup_plot()

    def setup_plot(self):
        """Set up the initial plot configuration"""
        self.ax.clear()
        self.ax.set_facecolor(COLORS['background'])
        self.ax.tick_params(colors=COLORS['text'])
        self.ax.spines['bottom'].set_color(COLORS['text'])
        self.ax.spines['top'].set_color(COLORS['text'])
        self.ax.spines['right'].set_color(COLORS['text'])
        self.ax.spines['left'].set_color(COLORS['text'])

        # Set labels
        self.ax.set_xlabel('Array Index', color=COLORS['text'])
        self.ax.set_ylabel('Value', color=COLORS['text'])
        self.ax.set_title('Sorting Algorithm Visualization', color=COLORS['text'])

        self.canvas.draw()

    def draw_array(self, array_data, colors=None):
        """
        Draw the array as bars

        Args:
            array_data: List of numbers to visualize
            colors: Optional list of colors for each bar
        """
        self.array_data = array_data.copy()

        if colors is None:
            self.bar_colors = [self.color_manager.get_bar_color('default')] * len(array_data)
        else:
            self.bar_colors = colors

        self.redraw_bars()

    def redraw_bars(self):
        """Redraw all bars with current data and colors"""
        self.ax.clear()

        if not self.array_data:
            self.setup_plot()
            return

        # Create x positions
        x_positions = np.arange(len(self.array_data))

        # Create bars
        self.bars = self.ax.bar(
            x_positions, 
            self.array_data, 
            color=self.bar_colors,
            edgecolor='white',
            linewidth=0.5
        )

        # Customize plot
        self.ax.set_facecolor(COLORS['background'])
        self.ax.set_xlabel('Array Index', color=COLORS['text'])
        self.ax.set_ylabel('Value', color=COLORS['text'])
        self.ax.set_title('Sorting Algorithm Visualization', color=COLORS['text'])

        # Set axis properties
        self.ax.tick_params(colors=COLORS['text'])
        for spine in self.ax.spines.values():
            spine.set_color(COLORS['text'])

        # Set limits
        self.ax.set_xlim(-0.5, len(self.array_data) - 0.5)
        if self.array_data:
            self.ax.set_ylim(0, max(self.array_data) * 1.1)

        # Add value labels for small arrays
        if len(self.array_data) <= 20:
            for i, (bar, value) in enumerate(zip(self.bars, self.array_data)):
                height = bar.get_height()
                self.ax.text(
                    bar.get_x() + bar.get_width()/2., 
                    height + max(self.array_data) * 0.01,
                    str(value), 
                    ha='center', 
                    va='bottom',
                    color=COLORS['text'],
                    fontsize=8
                )

        self.canvas.draw()

    def update_visualization(self, operation, indices, array_state):
        """
        Update the visualization based on algorithm operation

        Args:
            operation: Type of operation ('compare', 'swap', 'sorted', etc.)
            indices: List of indices involved in the operation
            array_state: Current state of the array
        """
        self.array_data = array_state.copy()

        # Reset all colors to default
        self.bar_colors = [self.color_manager.get_bar_color('default')] * len(self.array_data)

        # Color bars based on operation
        if operation == 'compare':
            for idx in indices:
                if 0 <= idx < len(self.bar_colors):
                    self.bar_colors[idx] = self.color_manager.get_bar_color('comparing')

        elif operation == 'swap':
            for idx in indices:
                if 0 <= idx < len(self.bar_colors):
                    self.bar_colors[idx] = self.color_manager.get_bar_color('swapping')

        elif operation == 'sorted':
            for idx in indices:
                if 0 <= idx < len(self.bar_colors):
                    self.bar_colors[idx] = self.color_manager.get_bar_color('sorted')

        elif operation == 'pivot':
            for idx in indices:
                if 0 <= idx < len(self.bar_colors):
                    self.bar_colors[idx] = self.color_manager.get_bar_color('pivot')

        elif operation in ['merge', 'insert', 'shift']:
            for idx in indices:
                if 0 <= idx < len(self.bar_colors):
                    self.bar_colors[idx] = self.color_manager.get_bar_color('current')

        # Redraw with updated colors
        self.redraw_bars()

    def mark_all_sorted(self):
        """Mark all bars as sorted (green)"""
        self.bar_colors = [self.color_manager.get_bar_color('sorted')] * len(self.array_data)
        self.redraw_bars()

    def clear_canvas(self):
        """Clear the canvas"""
        self.array_data = []
        self.bar_colors = []
        self.bars = []
        self.setup_plot()
