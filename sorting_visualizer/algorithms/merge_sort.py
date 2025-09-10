"""
Merge Sort Algorithm Implementation
Divides the array into halves, sorts them separately, then merges the sorted halves.
"""

import time
from .base_algorithm import BaseAlgorithm

class MergeSort(BaseAlgorithm):
    def sort(self):
        """
        Implement merge sort algorithm with visualization
        """
        self.start_time = time.time()
        self._merge_sort_recursive(0, len(self.array) - 1)
        self.end_time = time.time()

        # Mark all elements as sorted
        if self.is_running:
            self.mark_sorted(list(range(len(self.array))))

    def _merge_sort_recursive(self, left, right):
        """
        Recursive merge sort implementation
        """
        if not self.is_running or left >= right:
            return

        # Find the middle point
        mid = (left + right) // 2

        # Sort first and second halves
        self._merge_sort_recursive(left, mid)
        self._merge_sort_recursive(mid + 1, right)

        # Merge the sorted halves
        if self.is_running:
            self._merge(left, mid, right)

    def _merge(self, left, mid, right):
        """
        Merge two sorted subarrays
        """
        if not self.is_running:
            return

        # Create temporary arrays for left and right subarrays
        left_arr = self.array[left:mid + 1]
        right_arr = self.array[mid + 1:right + 1]

        # Initial indexes for left, right and merged arrays
        i = j = 0
        k = left

        # Merge the temporary arrays back into array[left..right]
        while i < len(left_arr) and j < len(right_arr) and self.is_running:
            # Compare elements from left and right subarrays
            self.update_callback('compare', [left + i, mid + 1 + j], self.array.copy())
            self.comparisons += 1

            if left_arr[i] <= right_arr[j]:
                self.array[k] = left_arr[i]
                i += 1
            else:
                self.array[k] = right_arr[j]
                j += 1

            # Update visualization
            self.update_callback('merge', [k], self.array.copy())
            k += 1

        # Copy remaining elements
        while i < len(left_arr) and self.is_running:
            self.array[k] = left_arr[i]
            self.update_callback('merge', [k], self.array.copy())
            i += 1
            k += 1

        while j < len(right_arr) and self.is_running:
            self.array[k] = right_arr[j]
            self.update_callback('merge', [k], self.array.copy())
            j += 1
            k += 1

    def get_complexity_info(self):
        """Return complexity information for merge sort"""
        return {
            'name': 'Merge Sort',
            'time_best': 'O(n log n)',
            'time_average': 'O(n log n)',
            'time_worst': 'O(n log n)',
            'space': 'O(n)',
            'stable': True,
            'in_place': False,
            'description': (
                "Uses divide-and-conquer approach by dividing the array "
                "into halves, sorting them separately, then merging the "
                "sorted halves together."
            )
        }
