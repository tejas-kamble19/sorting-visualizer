"""
Sorting algorithms package
Contains implementations of various sorting algorithms
"""

from .bubble_sort import BubbleSort
from .insertion_sort import InsertionSort
from .selection_sort import SelectionSort
from .merge_sort import MergeSort
from .quick_sort import QuickSort
from .heap_sort import HeapSort

# Algorithm registry
ALGORITHMS = {
    'bubble_sort': BubbleSort,
    'insertion_sort': InsertionSort,
    'selection_sort': SelectionSort,
    'merge_sort': MergeSort,
    'quick_sort': QuickSort,
    'heap_sort': HeapSort
}

def get_algorithm_by_name(name, array, callback):
    """
    Get algorithm instance by name

    Args:
        name: Algorithm name
        array: Array to sort
        callback: Callback function for visualization

    Returns:
        Algorithm instance
    """
    if name not in ALGORITHMS:
        raise ValueError(f"Unknown algorithm: {name}")

    return ALGORITHMS[name](array, callback)

def get_available_algorithms():
    """
    Get list of available algorithm names

    Returns:
        List of algorithm names
    """
    return list(ALGORITHMS.keys())
