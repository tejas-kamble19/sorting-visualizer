"""
Unit tests for sorting algorithms
"""

import unittest
from algorithms.bubble_sort import BubbleSort
from algorithms.insertion_sort import InsertionSort
from algorithms.selection_sort import SelectionSort
from algorithms.merge_sort import MergeSort
from algorithms.quick_sort import QuickSort
from algorithms.heap_sort import HeapSort

class TestSortingAlgorithms(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures"""
        self.test_arrays = [
            [64, 34, 25, 12, 22, 11, 90],
            [5, 2, 4, 6, 1, 3],
            [1],
            [],
            [3, 3, 3, 3],
            list(range(10, 0, -1))  # Reverse sorted
        ]

        # Dummy callback for testing
        self.callback = lambda op, idx, arr: None

    def test_bubble_sort(self):
        """Test bubble sort algorithm"""
        for test_array in self.test_arrays:
            with self.subTest(array=test_array):
                sorter = BubbleSort(test_array, self.callback)
                sorter.sort()
                self.assertEqual(sorter.array, sorted(test_array))

    def test_insertion_sort(self):
        """Test insertion sort algorithm"""
        for test_array in self.test_arrays:
            with self.subTest(array=test_array):
                sorter = InsertionSort(test_array, self.callback)
                sorter.sort()
                self.assertEqual(sorter.array, sorted(test_array))

    def test_selection_sort(self):
        """Test selection sort algorithm"""
        for test_array in self.test_arrays:
            with self.subTest(array=test_array):
                sorter = SelectionSort(test_array, self.callback)
                sorter.sort()
                self.assertEqual(sorter.array, sorted(test_array))

    def test_merge_sort(self):
        """Test merge sort algorithm"""
        for test_array in self.test_arrays:
            with self.subTest(array=test_array):
                sorter = MergeSort(test_array, self.callback)
                sorter.sort()
                self.assertEqual(sorter.array, sorted(test_array))

    def test_quick_sort(self):
        """Test quick sort algorithm"""
        for test_array in self.test_arrays:
            with self.subTest(array=test_array):
                sorter = QuickSort(test_array, self.callback)
                sorter.sort()
                self.assertEqual(sorter.array, sorted(test_array))

    def test_heap_sort(self):
        """Test heap sort algorithm"""
        for test_array in self.test_arrays:
            with self.subTest(array=test_array):
                sorter = HeapSort(test_array, self.callback)
                sorter.sort()
                self.assertEqual(sorter.array, sorted(test_array))

    def test_algorithm_properties(self):
        """Test that algorithms return correct complexity information"""
        algorithms = [BubbleSort, InsertionSort, SelectionSort, MergeSort, QuickSort, HeapSort]

        for algorithm_class in algorithms:
            with self.subTest(algorithm=algorithm_class.__name__):
                sorter = algorithm_class([1, 2, 3], self.callback)
                info = sorter.get_complexity_info()

                # Check that required fields are present
                required_fields = ['name', 'time_best', 'time_average', 'time_worst', 
                                 'space', 'stable', 'in_place', 'description']

                for field in required_fields:
                    self.assertIn(field, info)
                    self.assertIsNotNone(info[field])

if __name__ == '__main__':
    unittest.main()
