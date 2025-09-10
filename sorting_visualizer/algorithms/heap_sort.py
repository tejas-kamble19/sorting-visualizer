"""
Heap Sort Algorithm Implementation
Builds a max heap from the array, then repeatedly extracts the maximum element.
"""

import time
from .base_algorithm import BaseAlgorithm

class HeapSort(BaseAlgorithm):
    def sort(self):
        """
        Implement heap sort algorithm with visualization
        """
        self.start_time = time.time()
        n = len(self.array)

        # Build max heap
        for i in range(n // 2 - 1, -1, -1):
            if not self.is_running:
                break
            self._heapify(n, i)

        # Extract elements from heap one by one
        for i in range(n - 1, 0, -1):
            if not self.is_running:
                break

            # Move current root to end
            self.swap(0, i)
            self.mark_sorted(i)

            # Call heapify on the reduced heap
            self._heapify(i, 0)

        if self.is_running:
            self.mark_sorted(0)  # Mark first element as sorted

        self.end_time = time.time()

    def _heapify(self, n, i):
        """
        Heapify a subtree rooted with node i
        """
        if not self.is_running:
            return

        largest = i  # Initialize largest as root
        left = 2 * i + 1  # Left child
        right = 2 * i + 2  # Right child

        # If left child exists and is greater than root
        if left < n and self.compare(largest, left):  # array[largest] < array[left]
            largest = left

        # If right child exists and is greater than largest so far
        if right < n and self.compare(largest, right):  # array[largest] < array[right]
            largest = right

        # If largest is not root
        if largest != i and self.is_running:
            self.swap(i, largest)

            # Recursively heapify the affected sub-tree
            self._heapify(n, largest)

    def get_complexity_info(self):
        """Return complexity information for heap sort"""
        return {
            'name': 'Heap Sort',
            'time_best': 'O(n log n)',
            'time_average': 'O(n log n)',
            'time_worst': 'O(n log n)',
            'space': 'O(1)',
            'stable': False,
            'in_place': True,
            'description': (
                "Builds a max heap from the input array, then repeatedly "
                "extracts the maximum element and places it at the end of "
                "the sorted array."
            )
        }
