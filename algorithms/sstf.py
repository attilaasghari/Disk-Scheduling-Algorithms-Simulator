# sstf.py

def sstf(requests, head_position):
    """
    SSTF Disk Scheduling Algorithm
    :param requests: List of disk requests (cylinder numbers)
    :param head_position: Initial position of the disk head
    :return: The sequence of head movements and the total head movement
    """
    sequence = [head_position]
    total_head_movement = 0
    
    while requests:
        # Find the request with the minimum seek time
        closest_request = min(requests, key=lambda x: abs(x - sequence[-1]))
        total_head_movement += abs(sequence[-1] - closest_request)
        sequence.append(closest_request)
        requests.remove(closest_request)
    
    return sequence, total_head_movement
