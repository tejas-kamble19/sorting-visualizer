"""
Base class for all sorting algorithms
All sorting algorithms inherit from this class
"""

import time
from abc import ABC, abstractmethod

class BaseAlgorithm(ABC):
    def __init__(self, array, update_callback):
        """
        Initialize the algorithm

        Args:
            array: List of numbers to sort
            update_callback: Function to call for visualization updates
        """
        self.original_array = array.copy()
        self.array = array.copy()
        self.update_callback = update_callback

        # Statistics tracking
        self.comparisons = 0
        self.swaps = 0
        self.start_time = None
        self.end_time = None
        self.is_running = True

    @abstractmethod
    def sort(self):
        """
        Main sorting method - must be implemented by each algorithm
        This is where the actual sorting logic goes
        """
        pass

    @abstractmethod
    def get_complexity_info(self):
        """
        Return complexity information for this algorithm
        Must be implemented by each algorithm
        """
        pass

    def compare(self, i, j):
        """
        Compare two elements and notify the visualizer

        Args:
            i, j: Indices to compare

        Returns:
            True if array[i] > array[j], False otherwise
        """
        if not self.is_running:
            return False

        self.comparisons += 1

        # Notify visualizer about comparison
        self.update_callback('compare', [i, j], self.array.copy())

        return self.array[i] > self.array[j]

    def swap(self, i, j):
        """
        Swap two elements and notify the visualizer

        Args:
            i, j: Indices to swap
        """
        if not self.is_running:
            return

        if i != j:  # Only swap if indices are different
            self.swaps += 1

            # Perform the swap
            self.array[i], self.array[j] = self.array[j], self.array[i]

            # Notify visualizer about swap
            self.update_callback('swap', [i, j], self.array.copy())

    def mark_sorted(self, indices):
        """
        Mark positions as sorted (final position)

        Args:
            indices: List of indices that are now in final position
        """
        if not self.is_running:
            return

        if not isinstance(indices, list):
            indices = [indices]

        self.update_callback('sorted', indices, self.array.copy())

    def mark_pivot(self, index):
        """
        Mark an element as pivot (used in quicksort)

        Args:
            index: Index of the pivot element
        """
        if not self.is_running:
            return

        self.update_callback('pivot', [index], self.array.copy())

    def get_statistics(self):
        """
        Get performance statistics

        Returns:
            Dictionary containing performance metrics
        """
        elapsed_time = 0
        if self.start_time and self.end_time:
            elapsed_time = self.end_time - self.start_time

        return {
            'comparisons': self.comparisons,
            'swaps': self.swaps,
            'time': elapsed_time,
            'array_size': len(self.original_array)
        }

    def reset(self):
        """Reset the algorithm to initial state"""
        self.array = self.original_array.copy()
        self.comparisons = 0
        self.swaps = 0
        self.start_time = None
        self.end_time = None
        self.is_running = True

    def stop(self):
        """Stop the algorithm execution"""
        self.is_running = False

    def is_sorted(self):
        """Check if the array is sorted"""
        for i in range(len(self.array) - 1):
            if self.array[i] > self.array[i + 1]:
                return False
        return True
