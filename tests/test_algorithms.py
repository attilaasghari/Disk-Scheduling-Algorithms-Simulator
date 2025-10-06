"""
Tests for disk scheduling algorithms.
"""

import unittest
from src.disk_scheduling_simulator.algorithms import DiskScheduler

class TestDiskSchedulingAlgorithms(unittest.TestCase):
    
    def setUp(self):
        self.scheduler = DiskScheduler(disk_size=200, initial_head=50)
        self.requests = [98, 183, 37, 122, 14, 124, 65, 67]
    
    def test_fcfs(self):
        sequence, total = self.scheduler.run_algorithm("FCFS", self.requests)
        expected_sequence = [50, 98, 183, 37, 122, 14, 124, 65, 67]
        self.assertEqual(sequence, expected_sequence)
        # Calculate expected total movement
        expected_total = (48 + 85 + 146 + 85 + 108 + 110 + 59 + 2)
        self.assertEqual(total, expected_total)
    
    def test_sstf(self):
        sequence, total = self.scheduler.run_algorithm("SSTF", self.requests)
        # SSTF should start with closest request to 50, which is 65 or 67 or 37
        # 65 is closest (distance 15)
        self.assertEqual(sequence[0], 50)
        self.assertIn(sequence[1], [65, 67, 37])  # Could be any of these
        # Total movement should be less than FCFS
        self.assertLess(total, 642)  # FCFS total for this sequence
    
    def test_scan_right(self):
        sequence, total = self.scheduler.run_algorithm("SCAN", self.requests, "Right")
        # Should go right first, then left
        self.assertEqual(sequence[0], 50)
        # After 50, should go to next higher request: 65, 67, 98, 122, 124, 183
        # Then to end (199), then back to lower requests: 37, 14
        self.assertTrue(sequence[-1] in [14, 37])
    
    def test_scan_left(self):
        sequence, total = self.scheduler.run_algorithm("SCAN", self.requests, "Left")
        # Should go left first, then right
        self.assertEqual(sequence[0], 50)
        # After 50, should go to lower requests: 37, 14
        # Then to beginning (0), then to higher requests: 65, 67, 98, 122, 124, 183
        self.assertTrue(sequence[1] in [37, 14])
    
    def test_c_scan_right(self):
        sequence, total = self.scheduler.run_algorithm("C-SCAN", self.requests, "Right")
        # Should go right to end, then jump to beginning and continue right
        self.assertEqual(sequence[0], 50)
        # Last few should be the left requests in ascending order
        left_requests = [r for r in self.requests if r < 50]
        if left_requests:
            self.assertEqual(sequence[-1], max(left_requests))
    
    def test_look_right(self):
        sequence, total = self.scheduler.run_algorithm("LOOK", self.requests, "Right")
        # Similar to SCAN but doesn't go to end
        self.assertEqual(sequence[0], 50)
        # Should end with the lowest request
        self.assertEqual(sequence[-1], min(self.requests))
    
    def test_c_look_right(self):
        sequence, total = self.scheduler.run_algorithm("C-LOOK", self.requests, "Right")
        # Should end with the highest left request
        left_requests = [r for r in self.requests if r < 50]
        if left_requests:
            self.assertEqual(sequence[-1], max(left_requests))

if __name__ == '__main__':
    unittest.main()