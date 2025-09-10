"""
Configuration settings for the Sorting Algorithm Visualizer
All constants and settings are defined here
"""

# Application Configuration
APP_CONFIG = {
    'APP_NAME': 'Sorting Algorithm Visualizer',
    'VERSION': '1.0.0',
    'WINDOW_WIDTH': 1200,
    'WINDOW_HEIGHT': 800,
    'MIN_WINDOW_WIDTH': 800,
    'MIN_WINDOW_HEIGHT': 600,
}

# Animation Settings
ANIMATION_CONFIG = {
    'SPEED_MIN': 1,
    'SPEED_MAX': 10,
    'SPEED_DEFAULT': 5,
    'DELAY_BASE': 100,  # milliseconds
}

# Array Settings
ARRAY_CONFIG = {
    'SIZE_MIN': 10,
    'SIZE_MAX': 200,
    'SIZE_DEFAULT': 50,
    'VALUE_MIN': 10,
    'VALUE_MAX': 400,
}

# Visual Settings
VISUAL_CONFIG = {
    'CANVAS_WIDTH': 800,
    'CANVAS_HEIGHT': 500,
    'BAR_GAP_RATIO': 0.1,
    'BAR_MIN_WIDTH': 2,
}

# Color Scheme
COLORS = {
    'background': '#2C3E50',
    'surface': '#34495E',
    'primary': '#3498DB',
    'secondary': '#2ECC71',
    'accent': '#E74C3C',
    'text': '#ECF0F1',
    'text_secondary': '#BDC3C7',

    # Bar colors for different states
    'bar_default': '#3498DB',
    'bar_comparing': '#E74C3C',
    'bar_swapping': '#F39C12',
    'bar_sorted': '#2ECC71',
    'bar_pivot': '#9B59B6',
    'bar_current': '#1ABC9C',
}

# Algorithm Complexity Data
ALGORITHM_COMPLEXITY = {
    'bubble_sort': {
        'name': 'Bubble Sort',
        'time_best': 'O(n)',
        'time_average': 'O(n²)',
        'time_worst': 'O(n²)',
        'space': 'O(1)',
        'stable': True,
        'in_place': True,
        'description': 'Repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order.'
    },
    'insertion_sort': {
        'name': 'Insertion Sort',
        'time_best': 'O(n)',
        'time_average': 'O(n²)',
        'time_worst': 'O(n²)',
        'space': 'O(1)',
        'stable': True,
        'in_place': True,
        'description': 'Builds the final sorted array one item at a time, inserting each element into its correct position.'
    },
    'selection_sort': {
        'name': 'Selection Sort',
        'time_best': 'O(n²)',
        'time_average': 'O(n²)',
        'time_worst': 'O(n²)',
        'space': 'O(1)',
        'stable': False,
        'in_place': True,
        'description': 'Finds the minimum element and places it at the beginning, then repeats for remaining elements.'
    },
    'merge_sort': {
        'name': 'Merge Sort',
        'time_best': 'O(n log n)',
        'time_average': 'O(n log n)',
        'time_worst': 'O(n log n)',
        'space': 'O(n)',
        'stable': True,
        'in_place': False,
        'description': 'Divides the array into halves, sorts them separately, then merges the sorted halves.'
    },
    'quick_sort': {
        'name': 'Quick Sort',
        'time_best': 'O(n log n)',
        'time_average': 'O(n log n)',
        'time_worst': 'O(n²)',
        'space': 'O(log n)',
        'stable': False,
        'in_place': True,
        'description': 'Selects a pivot element and partitions the array around it, then recursively sorts the partitions.'
    },
    'heap_sort': {
        'name': 'Heap Sort',
        'time_best': 'O(n log n)',
        'time_average': 'O(n log n)',
        'time_worst': 'O(n log n)',
        'space': 'O(1)',
        'stable': False,
        'in_place': True,
        'description': 'Builds a max heap from the array, then repeatedly extracts the maximum element.'
    }
}
