"""
Quick Sort Algorithm Implementation
Selects a pivot element and partitions the array around it, then recursively sorts the partitions.
"""

import time
from .base_algorithm import BaseAlgorithm

class QuickSort(BaseAlgorithm):
    def sort(self):
        """
        Implement quick sort algorithm with visualization
        """
        self.start_time = time.time()
        self._quick_sort_recursive(0, len(self.array) - 1)
        self.end_time = time.time()

        # Mark all elements as sorted
        if self.is_running:
            self.mark_sorted(list(range(len(self.array))))

    def _quick_sort_recursive(self, low, high):
        """
        Recursive quick sort implementation
        """
        if not self.is_running or low < high:
            # Partition the array and get pivot index
            if self.is_running:
                pivot_index = self._partition(low, high)

                # Recursively sort elements before and after partition
                self._quick_sort_recursive(low, pivot_index - 1)
                self._quick_sort_recursive(pivot_index + 1, high)

    def _partition(self, low, high):
        """
        Partition function for quick sort
        """
        if not self.is_running:
            return low

        # Choose rightmost element as pivot
        pivot = self.array[high]
        self.mark_pivot(high)

        # Index of smaller element
        i = low - 1

        for j in range(low, high):
            if not self.is_running:
                break

            # Compare current element with pivot
            if not self.compare(j, high):  # array[j] <= pivot
                i += 1
                if i != j:
                    self.swap(i, j)

        # Place pivot in correct position
        if self.is_running:
            self.swap(i + 1, high)
            self.mark_sorted(i + 1)

        return i + 1

    def get_complexity_info(self):
        """Return complexity information for quick sort"""
        return {
            'name': 'Quick Sort',
            'time_best': 'O(n log n)',
            'time_average': 'O(n log n)',
            'time_worst': 'O(n²)',
            'space': 'O(log n)',
            'stable': False,
            'in_place': True,
            'description': (
                "Selects a 'pivot' element and partitions the array around it, "
                "then recursively applies the same strategy to the sub-arrays."
            )
        }
