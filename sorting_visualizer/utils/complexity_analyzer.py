"""
Performance analysis and complexity calculation utilities
"""

import time
from config.settings import ALGORITHM_COMPLEXITY

class ComplexityAnalyzer:
    def __init__(self):
        """Initialize the complexity analyzer"""
        self.benchmark_results = {}

    def get_algorithm_complexity(self, algorithm_name):
        """
        Get complexity information for an algorithm

        Args:
            algorithm_name: Name of the algorithm

        Returns:
            Dictionary with complexity information
        """
        return ALGORITHM_COMPLEXITY.get(algorithm_name, {
            'name': 'Unknown Algorithm',
            'time_best': 'N/A',
            'time_average': 'N/A',
            'time_worst': 'N/A',
            'space': 'N/A',
            'stable': False,
            'in_place': False,
            'description': 'No information available'
        })

    def analyze_performance(self, algorithm_instance):
        """
        Analyze the performance of an algorithm instance

        Args:
            algorithm_instance: Instance of a sorting algorithm

        Returns:
            Dictionary with performance metrics
        """
        stats = algorithm_instance.get_statistics()
        complexity_info = algorithm_instance.get_complexity_info()

        # Calculate efficiency metrics
        n = stats['array_size']
        comparisons_per_element = stats['comparisons'] / n if n > 0 else 0
        swaps_per_element = stats['swaps'] / n if n > 0 else 0

        return {
            'algorithm': complexity_info['name'],
            'array_size': n,
            'comparisons': stats['comparisons'],
            'swaps': stats['swaps'],
            'time_elapsed': stats['time'],
            'comparisons_per_element': comparisons_per_element,
            'swaps_per_element': swaps_per_element,
            'theoretical_complexity': {
                'time_best': complexity_info['time_best'],
                'time_average': complexity_info['time_average'],
                'time_worst': complexity_info['time_worst'],
                'space': complexity_info['space']
            },
            'properties': {
                'stable': complexity_info['stable'],
                'in_place': complexity_info['in_place']
            }
        }

    def compare_algorithms(self, results_list):
        """
        Compare multiple algorithm results

        Args:
            results_list: List of performance analysis results

        Returns:
            Dictionary with comparison data
        """
        if not results_list:
            return {}

        comparison = {
            'fastest_time': min(results_list, key=lambda x: x['time_elapsed']),
            'fewest_comparisons': min(results_list, key=lambda x: x['comparisons']),
            'fewest_swaps': min(results_list, key=lambda x: x['swaps']),
            'most_efficient_comparisons': min(results_list, key=lambda x: x['comparisons_per_element']),
            'stable_algorithms': [r for r in results_list if r['properties']['stable']],
            'in_place_algorithms': [r for r in results_list if r['properties']['in_place']]
        }

        return comparison

    def estimate_complexity_class(self, array_size, operations):
        """
        Estimate the complexity class based on actual operations

        Args:
            array_size: Size of the input array
            operations: Number of operations performed

        Returns:
            String describing the estimated complexity
        """
        n = array_size
        if n <= 1:
            return "O(1)"

        # Calculate ratios for different complexity classes
        linear_ratio = operations / n
        nlogn_ratio = operations / (n * (n.bit_length() - 1)) if n > 1 else float('inf')
        quadratic_ratio = operations / (n * n)

        # Determine which complexity class fits best
        if quadratic_ratio <= 2:
            return "O(n²)"
        elif nlogn_ratio <= 10:
            return "O(n log n)"
        elif linear_ratio <= 5:
            return "O(n)"
        else:
            return "O(n²) or higher"

    def benchmark_algorithm(self, algorithm_class, test_arrays, callback_func=None):
        """
        Benchmark an algorithm on multiple test cases

        Args:
            algorithm_class: Algorithm class to benchmark
            test_arrays: List of arrays to test on
            callback_func: Optional callback for visualization

        Returns:
            List of benchmark results
        """
        results = []

        for i, test_array in enumerate(test_arrays):
            # Use dummy callback if none provided
            dummy_callback = callback_func or (lambda op, idx, arr: None)

            # Create algorithm instance
            algorithm = algorithm_class(test_array, dummy_callback)

            # Run the algorithm
            start_time = time.time()
            algorithm.sort()
            end_time = time.time()

            # Analyze results
            analysis = self.analyze_performance(algorithm)
            analysis['test_case'] = i
            analysis['estimated_complexity'] = self.estimate_complexity_class(
                len(test_array), 
                analysis['comparisons'] + analysis['swaps']
            )

            results.append(analysis)

        return results
