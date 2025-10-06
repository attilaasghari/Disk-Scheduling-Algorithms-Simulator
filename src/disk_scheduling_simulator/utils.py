"""
Utility functions for the disk scheduling simulator.
"""

def validate_requests(requests, disk_size):
    """
    Validate that all requests are within disk boundaries.
    
    Args:
        requests (list): List of disk requests
        disk_size (int): Total number of cylinders
        
    Returns:
        bool: True if all requests are valid, False otherwise
    """
    return all(0 <= req < disk_size for req in requests)

def calculate_total_movement(sequence):
    """
    Calculate total head movement from a sequence of positions.
    
    Args:
        sequence (list): Sequence of head positions
        
    Returns:
        int: Total head movement
    """
    return sum(abs(sequence[i] - sequence[i-1]) for i in range(1, len(sequence)))