"""
Selection Sort Algorithm Implementation
Finds the minimum element and places it at the beginning, then repeats for remaining elements.
"""

import time
from .base_algorithm import BaseAlgorithm

class SelectionSort(BaseAlgorithm):
    def sort(self):
        """
        Implement selection sort algorithm with visualization
        """
        self.start_time = time.time()
        n = len(self.array)

        # Move boundary of unsorted subarray
        for i in range(n):
            if not self.is_running:
                break

            # Find the minimum element in remaining unsorted array
            min_idx = i

            for j in range(i + 1, n):
                if not self.is_running:
                    break

                # Compare with current minimum
                if self.compare(min_idx, j):  # array[min_idx] > array[j]
                    min_idx = j

            # Swap the found minimum element with the first element
            if self.is_running and min_idx != i:
                self.swap(i, min_idx)

            # Mark current position as sorted
            if self.is_running:
                self.mark_sorted(i)

        self.end_time = time.time()

    def get_complexity_info(self):
        """Return complexity information for selection sort"""
        return {
            'name': 'Selection Sort',
            'time_best': 'O(n²)',
            'time_average': 'O(n²)',
            'time_worst': 'O(n²)',
            'space': 'O(1)',
            'stable': False,
            'in_place': True,
            'description': (
                "Finds the minimum element from the unsorted part and "
                "places it at the beginning. Repeats this process for "
                "the remaining elements."
            )
        }
