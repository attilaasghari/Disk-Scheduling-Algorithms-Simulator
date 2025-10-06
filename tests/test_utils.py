"""
Tests for utility functions.
"""

import unittest
from src.disk_scheduling_simulator.utils import validate_requests, calculate_total_movement

class TestUtils(unittest.TestCase):
    
    def test_validate_requests_valid(self):
        requests = [10, 50, 100, 150]
        self.assertTrue(validate_requests(requests, 200))
    
    def test_validate_requests_invalid_low(self):
        requests = [-5, 50, 100]
        self.assertFalse(validate_requests(requests, 200))
    
    def test_validate_requests_invalid_high(self):
        requests = [50, 100, 250]
        self.assertFalse(validate_requests(requests, 200))
    
    def test_calculate_total_movement(self):
        sequence = [50, 60, 40, 70]
        expected = abs(60-50) + abs(40-60) + abs(70-40)  # 10 + 20 + 30 = 60
        self.assertEqual(calculate_total_movement(sequence), expected)

if __name__ == '__main__':
    unittest.main()