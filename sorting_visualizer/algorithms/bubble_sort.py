"""
Bubble Sort Algorithm Implementation
Simple sorting algorithm that repeatedly steps through the list,
compares adjacent elements and swaps them if they're in the wrong order.
"""

import time
from .base_algorithm import BaseAlgorithm

class BubbleSort(BaseAlgorithm):
    def sort(self):
        """
        Implement bubble sort algorithm with visualization
        """
        self.start_time = time.time()
        n = len(self.array)

        # Outer loop for each pass through the array
        for i in range(n):
            if not self.is_running:
                break

            swapped = False  # Flag to track if any swaps occurred

            # Inner loop to compare adjacent elements
            # Last i elements are already in place, so we can skip them
            for j in range(0, n - i - 1):
                if not self.is_running:
                    break

                # Compare adjacent elements
                if self.compare(j, j + 1):
                    # Swap if they're in wrong order
                    self.swap(j, j + 1)
                    swapped = True

            # After each pass, the largest element is in its final position
            if self.is_running:
                self.mark_sorted(n - i - 1)

            # If no swapping occurred, array is already sorted
            if not swapped:
                # Mark remaining elements as sorted
                for k in range(n - i - 1):
                    if self.is_running:
                        self.mark_sorted(k)
                break

        self.end_time = time.time()

    def get_complexity_info(self):
        """Return complexity information for bubble sort"""
        return {
            'name': 'Bubble Sort',
            'time_best': 'O(n)',
            'time_average': 'O(n²)',
            'time_worst': 'O(n²)',
            'space': 'O(1)',
            'stable': True,
            'in_place': True,
            'description': (
                "Repeatedly steps through the list, compares adjacent "
                "elements and swaps them if they're in the wrong order. "
                "The pass through the list is repeated until no swaps are needed."
            )
        }
