"""
Control panel with buttons, sliders, and algorithm information
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from config.settings import COLORS, ANIMATION_CONFIG, ARRAY_CONFIG, ALGORITHM_COMPLEXITY
from utils.complexity_analyzer import ComplexityAnalyzer

class ControlPanel(tk.Frame):
    def __init__(self, parent, main_window, **kwargs):
        """
        Initialize the control panel

        Args:
            parent: Parent widget
            main_window: Reference to main window
            **kwargs: Frame configuration options
        """
        super().__init__(parent, **kwargs)
        self.main_window = main_window
        self.complexity_analyzer = ComplexityAnalyzer()

        # Configure style
        self.configure(bg=COLORS['surface'])

        # Variables for UI controls
        self.algorithm_var = tk.StringVar(value='bubble_sort')
        self.speed_var = tk.IntVar(value=ANIMATION_CONFIG['SPEED_DEFAULT'])
        self.size_var = tk.IntVar(value=ARRAY_CONFIG['SIZE_DEFAULT'])

        # State variables
        self.is_sorting = False

        self.create_widgets()
        self.layout_widgets()
        self.bind_events()

    def create_widgets(self):
        """Create all control widgets"""
        # Main control frame
        self.control_frame = tk.LabelFrame(
            self, 
            text="Controls", 
            bg=COLORS['surface'],
            fg=COLORS['text'],
            font=('Arial', 12, 'bold')
        )

        # Algorithm selection
        tk.Label(
            self.control_frame, 
            text="Algorithm:", 
            bg=COLORS['surface'], 
            fg=COLORS['text']
        ).grid(row=0, column=0, sticky='w', padx=5, pady=5)

        self.algorithm_combo = ttk.Combobox(
            self.control_frame,
            textvariable=self.algorithm_var,
            values=[
                ('bubble_sort', 'Bubble Sort'),
                ('insertion_sort', 'Insertion Sort'),
                ('selection_sort', 'Selection Sort'),
                ('merge_sort', 'Merge Sort'),
                ('quick_sort', 'Quick Sort'),
                ('heap_sort', 'Heap Sort')
            ],
            state='readonly'
        )
        self.algorithm_combo['values'] = [
            'Bubble Sort',
            'Insertion Sort',
            'Selection Sort', 
            'Merge Sort',
            'Quick Sort',
            'Heap Sort'
        ]
        self.algorithm_combo.current(0)

        # Array size control
        tk.Label(
            self.control_frame, 
            text="Array Size:", 
            bg=COLORS['surface'], 
            fg=COLORS['text']
        ).grid(row=2, column=0, sticky='w', padx=5, pady=5)

        self.size_scale = tk.Scale(
            self.control_frame,
            from_=ARRAY_CONFIG['SIZE_MIN'],
            to=ARRAY_CONFIG['SIZE_MAX'],
            orient=tk.HORIZONTAL,
            variable=self.size_var,
            bg=COLORS['surface'],
            fg=COLORS['text'],
            highlightbackground=COLORS['surface']
        )

        # Animation speed control
        tk.Label(
            self.control_frame, 
            text="Animation Speed:", 
            bg=COLORS['surface'], 
            fg=COLORS['text']
        ).grid(row=4, column=0, sticky='w', padx=5, pady=5)

        self.speed_scale = tk.Scale(
            self.control_frame,
            from_=ANIMATION_CONFIG['SPEED_MIN'],
            to=ANIMATION_CONFIG['SPEED_MAX'],
            orient=tk.HORIZONTAL,
            variable=self.speed_var,
            bg=COLORS['surface'],
            fg=COLORS['text'],
            highlightbackground=COLORS['surface']
        )

        # Action buttons frame
        self.buttons_frame = tk.Frame(self.control_frame, bg=COLORS['surface'])

        # Generate array button
        self.generate_btn = tk.Button(
            self.buttons_frame,
            text="Generate Array",
            command=self.generate_array,
            bg=COLORS['primary'],
            fg='white',
            font=('Arial', 10, 'bold'),
            relief='raised',
            bd=2
        )

        # Start/Pause button
        self.start_btn = tk.Button(
            self.buttons_frame,
            text="Start",
            command=self.toggle_sorting,
            bg=COLORS['secondary'],
            fg='white',
            font=('Arial', 10, 'bold'),
            relief='raised',
            bd=2
        )

        # Reset button
        self.reset_btn = tk.Button(
            self.buttons_frame,
            text="Reset",
            command=self.reset_array,
            bg=COLORS['accent'],
            fg='white',
            font=('Arial', 10, 'bold'),
            relief='raised',
            bd=2
        )

        # Load file button
        self.load_btn = tk.Button(
            self.buttons_frame,
            text="Load File",
            command=self.load_from_file,
            bg=COLORS['text_secondary'],
            fg='white',
            font=('Arial', 10, 'bold'),
            relief='raised',
            bd=2
        )

        # Algorithm info frame
        self.info_frame = tk.LabelFrame(
            self,
            text="Algorithm Information",
            bg=COLORS['surface'],
            fg=COLORS['text'],
            font=('Arial', 12, 'bold')
        )

        # Algorithm description
        self.description_text = tk.Text(
            self.info_frame,
            height=4,
            width=30,
            wrap=tk.WORD,
            bg=COLORS['background'],
            fg=COLORS['text'],
            font=('Arial', 9),
            state='disabled'
        )

        # Complexity info frame
        self.complexity_frame = tk.Frame(self.info_frame, bg=COLORS['surface'])

        # Statistics frame
        self.stats_frame = tk.LabelFrame(
            self,
            text="Real-time Statistics",
            bg=COLORS['surface'],
            fg=COLORS['text'],
            font=('Arial', 12, 'bold')
        )

        # Statistics labels
        self.comparisons_label = tk.Label(
            self.stats_frame,
            text="Comparisons: 0",
            bg=COLORS['surface'],
            fg=COLORS['text']
        )

        self.swaps_label = tk.Label(
            self.stats_frame,
            text="Swaps: 0",
            bg=COLORS['surface'],
            fg=COLORS['text']
        )

        self.time_label = tk.Label(
            self.stats_frame,
            text="Time: 0.00s",
            bg=COLORS['surface'],
            fg=COLORS['text']
        )

    def layout_widgets(self):
        """Layout all widgets using grid"""
        # Main frames
        self.control_frame.pack(fill='x', padx=10, pady=5)
        self.info_frame.pack(fill='both', expand=True, padx=10, pady=5)
        self.stats_frame.pack(fill='x', padx=10, pady=5)

        # Control frame layout
        self.algorithm_combo.grid(row=1, column=0, columnspan=2, sticky='ew', padx=5, pady=2)
        self.size_scale.grid(row=3, column=0, columnspan=2, sticky='ew', padx=5, pady=2)
        self.speed_scale.grid(row=5, column=0, columnspan=2, sticky='ew', padx=5, pady=2)

        self.buttons_frame.grid(row=6, column=0, columnspan=2, pady=10)

        # Buttons layout
        self.generate_btn.pack(side='top', fill='x', pady=2)
        self.start_btn.pack(side='top', fill='x', pady=2)
        self.reset_btn.pack(side='top', fill='x', pady=2)
        self.load_btn.pack(side='top', fill='x', pady=2)

        # Info frame layout
        self.description_text.pack(fill='both', expand=True, padx=5, pady=5)
        self.complexity_frame.pack(fill='x', padx=5, pady=5)

        # Statistics layout
        self.comparisons_label.pack(anchor='w', padx=5, pady=2)
        self.swaps_label.pack(anchor='w', padx=5, pady=2)
        self.time_label.pack(anchor='w', padx=5, pady=2)

        # Configure column weights
        self.control_frame.columnconfigure(0, weight=1)

    def bind_events(self):
        """Bind event handlers"""
        self.algorithm_combo.bind('<<ComboboxSelected>>', self.on_algorithm_changed)
        self.size_scale.bind('<ButtonRelease-1>', self.on_size_changed)

    def on_algorithm_changed(self, event=None):
        """Handle algorithm selection change"""
        algorithm_name = self.get_selected_algorithm()
        self.update_algorithm_info(algorithm_name)

    def on_size_changed(self, event=None):
        """Handle array size change"""
        if not self.is_sorting:
            self.generate_array()

    def get_selected_algorithm(self):
        """Get currently selected algorithm name"""
        selection = self.algorithm_combo.get()
        algorithm_map = {
            'Bubble Sort': 'bubble_sort',
            'Insertion Sort': 'insertion_sort',
            'Selection Sort': 'selection_sort',
            'Merge Sort': 'merge_sort',
            'Quick Sort': 'quick_sort',
            'Heap Sort': 'heap_sort'
        }
        return algorithm_map.get(selection, 'bubble_sort')

    def get_array_size(self):
        """Get current array size setting"""
        return self.size_var.get()

    def get_animation_speed(self):
        """Get current animation speed setting"""
        return self.speed_var.get()

    def generate_array(self):
        """Generate new random array"""
        if hasattr(self.main_window, 'generate_new_array'):
            self.main_window.generate_new_array()

    def toggle_sorting(self):
        """Toggle between start and pause"""
        if self.is_sorting:
            if hasattr(self.main_window, 'pause_sorting'):
                self.main_window.pause_sorting()
        else:
            if hasattr(self.main_window, 'start_sorting'):
                self.main_window.start_sorting()

    def reset_array(self):
        """Reset array to original state"""
        if hasattr(self.main_window, 'reset_array'):
            self.main_window.reset_array()

    def load_from_file(self):
        """Load array from file"""
        filename = filedialog.askopenfilename(
            title="Load Array Data",
            filetypes=[
                ("Text files", "*.txt"),
                ("CSV files", "*.csv"),
                ("All files", "*.*")
            ]
        )

        if filename and hasattr(self.main_window, 'load_array_from_file'):
            try:
                self.main_window.load_array_from_file(filename)
            except Exception as e:
                messagebox.showerror("Error", f"Could not load file: {str(e)}")

    def update_algorithm_info(self, algorithm_name):
        """Update algorithm information display"""
        info = self.complexity_analyzer.get_algorithm_complexity(algorithm_name)

        # Update description
        self.description_text.config(state='normal')
        self.description_text.delete(1.0, tk.END)
        self.description_text.insert(1.0, info['description'])
        self.description_text.config(state='disabled')

        # Update complexity info
        for widget in self.complexity_frame.winfo_children():
            widget.destroy()

        complexity_text = f"""Time Complexity:
Best: {info['time_best']}
Average: {info['time_average']}  
Worst: {info['time_worst']}
Space: {info['space']}

Properties:
Stable: {'Yes' if info['stable'] else 'No'}
In-place: {'Yes' if info['in_place'] else 'No'}"""

        tk.Label(
            self.complexity_frame,
            text=complexity_text,
            bg=COLORS['surface'],
            fg=COLORS['text'],
            font=('Arial', 9),
            justify='left'
        ).pack(anchor='w')

    def set_sorting_state(self, sorting):
        """Update UI based on sorting state"""
        self.is_sorting = sorting

        if sorting:
            self.start_btn.config(text="Pause", bg=COLORS['accent'])
            self.algorithm_combo.config(state='disabled')
            self.generate_btn.config(state='disabled')
            self.load_btn.config(state='disabled')
        else:
            self.start_btn.config(text="Start", bg=COLORS['secondary'])
            self.algorithm_combo.config(state='readonly')
            self.generate_btn.config(state='normal')
            self.load_btn.config(state='normal')

    def update_statistics(self, comparisons=0, swaps=0, time_elapsed=0):
        """Update statistics display"""
        self.comparisons_label.config(text=f"Comparisons: {comparisons}")
        self.swaps_label.config(text=f"Swaps: {swaps}")
        self.time_label.config(text=f"Time: {time_elapsed:.2f}s")
