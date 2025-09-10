"""
Data generation utilities for creating test arrays
"""

import random
from config.settings import ARRAY_CONFIG

class DataGenerator:
    def __init__(self):
        """Initialize the data generator"""
        self.random = random.Random()  # For reproducible results

    def generate_random_array(self, size=None, min_val=None, max_val=None, seed=None):
        """
        Generate a random array of integers

        Args:
            size: Number of elements (default from config)
            min_val: Minimum value (default from config)
            max_val: Maximum value (default from config)
            seed: Random seed for reproducible results

        Returns:
            List of random integers
        """
        if seed is not None:
            self.random.seed(seed)

        size = size or ARRAY_CONFIG['SIZE_DEFAULT']
        min_val = min_val or ARRAY_CONFIG['VALUE_MIN']
        max_val = max_val or ARRAY_CONFIG['VALUE_MAX']

        return [self.random.randint(min_val, max_val) for _ in range(size)]

    def generate_sorted_array(self, size=None, ascending=True):
        """
        Generate a sorted array (best case for some algorithms)

        Args:
            size: Number of elements
            ascending: True for ascending, False for descending

        Returns:
            Sorted list of integers
        """
        size = size or ARRAY_CONFIG['SIZE_DEFAULT']
        min_val = ARRAY_CONFIG['VALUE_MIN']
        max_val = ARRAY_CONFIG['VALUE_MAX']

        step = (max_val - min_val) / (size - 1) if size > 1 else 0
        array = [int(min_val + i * step) for i in range(size)]

        if not ascending:
            array.reverse()

        return array

    def generate_reverse_sorted_array(self, size=None):
        """
        Generate a reverse-sorted array (worst case for some algorithms)

        Args:
            size: Number of elements

        Returns:
            Reverse-sorted list of integers
        """
        return self.generate_sorted_array(size, ascending=False)

    def generate_nearly_sorted_array(self, size=None, swaps=None):
        """
        Generate a nearly sorted array (interesting test case)

        Args:
            size: Number of elements
            swaps: Number of random swaps to make (default: size/10)

        Returns:
            Nearly sorted list of integers
        """
        size = size or ARRAY_CONFIG['SIZE_DEFAULT']
        swaps = swaps or max(1, size // 10)

        # Start with sorted array
        array = self.generate_sorted_array(size)

        # Make some random swaps
        for _ in range(swaps):
            i = self.random.randint(0, size - 1)
            j = self.random.randint(0, size - 1)
            array[i], array[j] = array[j], array[i]

        return array

    def generate_duplicate_heavy_array(self, size=None, unique_values=None):
        """
        Generate array with many duplicate values

        Args:
            size: Number of elements
            unique_values: Number of unique values to use

        Returns:
            List with many duplicate values
        """
        size = size or ARRAY_CONFIG['SIZE_DEFAULT']
        unique_values = unique_values or max(3, size // 5)

        min_val = ARRAY_CONFIG['VALUE_MIN']
        max_val = ARRAY_CONFIG['VALUE_MAX']

        # Generate unique values
        step = (max_val - min_val) / (unique_values - 1) if unique_values > 1 else 0
        values = [int(min_val + i * step) for i in range(unique_values)]

        # Create array by randomly selecting from unique values
        array = [self.random.choice(values) for _ in range(size)]

        return array

    def load_from_file(self, filename):
        """
        Load array data from a file

        Args:
            filename: Path to file containing numbers (one per line or comma-separated)

        Returns:
            List of numbers from file
        """
        try:
            with open(filename, 'r') as f:
                content = f.read().strip()

                # Try comma-separated first
                if ',' in content:
                    numbers = [int(x.strip()) for x in content.split(',')]
                else:
                    # Try line-separated
                    numbers = [int(line.strip()) for line in content.split('\n') if line.strip()]

                return numbers
        except (FileNotFoundError, ValueError) as e:
            raise ValueError(f"Could not load data from file: {e}")
