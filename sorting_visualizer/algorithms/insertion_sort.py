"""
Insertion Sort Algorithm Implementation
Builds the final sorted array one item at a time, inserting each element into its correct position.
"""

import time
from .base_algorithm import BaseAlgorithm

class InsertionSort(BaseAlgorithm):
    def sort(self):
        """
        Implement insertion sort algorithm with visualization
        """
        self.start_time = time.time()
        n = len(self.array)

        # Start from second element (index 1)
        for i in range(1, n):
            if not self.is_running:
                break

            # Current element to be inserted
            key = self.array[i]
            j = i - 1

            # Move elements that are greater than key one position ahead
            while j >= 0 and self.is_running:
                if not self.compare(j, i):  # array[j] <= key
                    break

                # Shift element to the right
                self.array[j + 1] = self.array[j]
                self.update_callback('shift', [j, j + 1], self.array.copy())
                j -= 1

            # Insert the key at correct position
            if self.is_running:
                self.array[j + 1] = key
                self.update_callback('insert', [j + 1], self.array.copy())
                self.mark_sorted(list(range(i + 1)))

        self.end_time = time.time()

    def get_complexity_info(self):
        """Return complexity information for insertion sort"""
        return {
            'name': 'Insertion Sort',
            'time_best': 'O(n)',
            'time_average': 'O(n²)',
            'time_worst': 'O(n²)',
            'space': 'O(1)',
            'stable': True,
            'in_place': True,
            'description': (
                "Builds the final sorted array one item at a time by "
                "inserting each element into its correct position within "
                "the already sorted portion."
            )
        }
