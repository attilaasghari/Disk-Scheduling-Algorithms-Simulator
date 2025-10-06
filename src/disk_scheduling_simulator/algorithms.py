"""
Implementation of disk scheduling algorithms.
"""

class DiskScheduler:
    """Class implementing various disk scheduling algorithms."""
    
    def __init__(self, disk_size=200, initial_head=0):
        """
        Initialize the disk scheduler.
        
        Args:
            disk_size (int): Total number of cylinders (default: 200)
            initial_head (int): Initial position of disk head (default: 0)
        """
        self.disk_size = disk_size
        self.initial_head = initial_head
        self.algorithms = {
            "FCFS": self._fcfs,
            "SSTF": self._sstf,
            "SCAN": self._scan,
            "C-SCAN": self._c_scan,
            "LOOK": self._look,
            "C-LOOK": self._c_look
        }
    
    def run_algorithm(self, algorithm_name, requests, direction="Right"):
        """
        Run the specified disk scheduling algorithm.
        
        Args:
            algorithm_name (str): Name of the algorithm to run
            requests (list): List of disk requests (cylinder numbers)
            direction (str): Direction for SCAN/LOOK algorithms ("Right" or "Left")
            
        Returns:
            tuple: (sequence of head movements, total head movement)
        """
        if algorithm_name not in self.algorithms:
            raise ValueError(f"Algorithm {algorithm_name} not implemented")
        
        return self.algorithms[algorithm_name](requests.copy(), direction)
    
    def _fcfs(self, requests, direction=None):
        """First-Come, First-Served algorithm."""
        sequence = [self.initial_head] + requests
        total_movement = sum(abs(sequence[i] - sequence[i-1]) for i in range(1, len(sequence)))
        return sequence, total_movement
    
    def _sstf(self, requests, direction=None):
        """Shortest Seek Time First algorithm."""
        current = self.initial_head
        sequence = [current]
        total_movement = 0
        
        while requests:
            closest = min(requests, key=lambda x: abs(x - current))
            total_movement += abs(closest - current)
            current = closest
            sequence.append(current)
            requests.remove(current)
        
        return sequence, total_movement
    
    def _scan(self, requests, direction):
        """SCAN (Elevator) algorithm."""
        requests = sorted(requests)
        current = self.initial_head
        sequence = [current]
        total_movement = 0
        
        if direction == "Right":
            right_requests = [r for r in requests if r >= current]
            right_requests.sort()
            for req in right_requests:
                total_movement += abs(req - current)
                current = req
                sequence.append(current)
            
            if current < self.disk_size - 1:
                total_movement += (self.disk_size - 1) - current
                current = self.disk_size - 1
                sequence.append(current)
            
            left_requests = [r for r in requests if r < self.initial_head]
            left_requests.sort(reverse=True)
            for req in left_requests:
                total_movement += abs(req - current)
                current = req
                sequence.append(current)
        else:  # Left
            left_requests = [r for r in requests if r <= current]
            left_requests.sort(reverse=True)
            for req in left_requests:
                total_movement += abs(req - current)
                current = req
                sequence.append(current)
            
            if current > 0:
                total_movement += current
                current = 0
                sequence.append(current)
            
            right_requests = [r for r in requests if r > self.initial_head]
            right_requests.sort()
            for req in right_requests:
                total_movement += abs(req - current)
                current = req
                sequence.append(current)
        
        return sequence, total_movement
    
    def _c_scan(self, requests, direction):
        """C-SCAN (Circular SCAN) algorithm."""
        requests = sorted(requests)
        current = self.initial_head
        sequence = [current]
        total_movement = 0
        
        if direction == "Right":
            right_requests = [r for r in requests if r >= current]
            right_requests.sort()
            for req in right_requests:
                total_movement += abs(req - current)
                current = req
                sequence.append(current)
            
            if right_requests or [r for r in requests if r < self.initial_head]:
                total_movement += (self.disk_size - 1) - current + (self.disk_size - 1)
                current = 0
                sequence.append(current)
            
            left_requests = [r for r in requests if r < self.initial_head]
            left_requests.sort()
            for req in left_requests:
                total_movement += abs(req - current)
                current = req
                sequence.append(current)
        else:  # Left
            left_requests = [r for r in requests if r <= current]
            left_requests.sort(reverse=True)
            for req in left_requests:
                total_movement += abs(req - current)
                current = req
                sequence.append(current)
            
            if left_requests or [r for r in requests if r > self.initial_head]:
                total_movement += current + (self.disk_size - 1)
                current = self.disk_size - 1
                sequence.append(current)
            
            right_requests = [r for r in requests if r > self.initial_head]
            right_requests.sort(reverse=True)
            for req in right_requests:
                total_movement += abs(req - current)
                current = req
                sequence.append(current)
        
        return sequence, total_movement
    
    def _look(self, requests, direction):
        """LOOK algorithm."""
        requests = sorted(requests)
        current = self.initial_head
        sequence = [current]
        total_movement = 0
        
        if direction == "Right":
            right_requests = [r for r in requests if r >= current]
            right_requests.sort()
            for req in right_requests:
                total_movement += abs(req - current)
                current = req
                sequence.append(current)
            
            left_requests = [r for r in requests if r < self.initial_head]
            left_requests.sort(reverse=True)
            for req in left_requests:
                total_movement += abs(req - current)
                current = req
                sequence.append(current)
        else:  # Left
            left_requests = [r for r in requests if r <= current]
            left_requests.sort(reverse=True)
            for req in left_requests:
                total_movement += abs(req - current)
                current = req
                sequence.append(current)
            
            right_requests = [r for r in requests if r > self.initial_head]
            right_requests.sort()
            for req in right_requests:
                total_movement += abs(req - current)
                current = req
                sequence.append(current)
        
        return sequence, total_movement
    
    def _c_look(self, requests, direction):
        """C-LOOK algorithm."""
        requests = sorted(requests)
        current = self.initial_head
        sequence = [current]
        total_movement = 0
        
        if direction == "Right":
            right_requests = [r for r in requests if r >= current]
            right_requests.sort()
            for req in right_requests:
                total_movement += abs(req - current)
                current = req
                sequence.append(current)
            
            if right_requests and [r for r in requests if r < self.initial_head]:
                left_requests = [r for r in requests if r < self.initial_head]
                first_left = min(left_requests)
                total_movement += current - first_left
                current = first_left
                sequence.append(current)
            
            left_requests = [r for r in requests if r < self.initial_head]
            left_requests.sort()
            for req in left_requests:
                total_movement += abs(req - current)
                current = req
                sequence.append(current)
        else:  # Left
            left_requests = [r for r in requests if r <= current]
            left_requests.sort(reverse=True)
            for req in left_requests:
                total_movement += abs(req - current)
                current = req
                sequence.append(current)
            
            if left_requests and [r for r in requests if r > self.initial_head]:
                right_requests = [r for r in requests if r > self.initial_head]
                last_right = max(right_requests)
                total_movement += last_right - current
                current = last_right
                sequence.append(current)
            
            right_requests = [r for r in requests if r > self.initial_head]
            right_requests.sort(reverse=True)
            for req in right_requests:
                total_movement += abs(req - current)
                current = req
                sequence.append(current)
        
        return sequence, total_movement