"""
Basic GUI component tests
"""

import unittest
import tkinter as tk
from gui.main_window import MainWindow
from utils.data_generator import DataGenerator

class TestGUIComponents(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures"""
        self.root = tk.Tk()
        self.root.withdraw()  # Hide window during tests

    def tearDown(self):
        """Clean up after tests"""
        self.root.destroy()

    def test_main_window_creation(self):
        """Test that main window can be created"""
        try:
            app = MainWindow(self.root)
            self.assertIsNotNone(app)
        except Exception as e:
            self.fail(f"MainWindow creation failed: {e}")

    def test_data_generator(self):
        """Test data generator functionality"""
        generator = DataGenerator()

        # Test random array generation
        array = generator.generate_random_array(size=10)
        self.assertEqual(len(array), 10)
        self.assertTrue(all(isinstance(x, int) for x in array))

        # Test sorted array generation
        sorted_array = generator.generate_sorted_array(size=5)
        self.assertEqual(sorted_array, sorted(sorted_array))

        # Test reverse sorted array
        reverse_array = generator.generate_reverse_sorted_array(size=5)
        self.assertEqual(reverse_array, sorted(reverse_array, reverse=True))

if __name__ == '__main__':
    unittest.main()
