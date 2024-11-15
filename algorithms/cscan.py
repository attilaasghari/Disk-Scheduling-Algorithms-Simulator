# cscan.py

def cscan(requests, head_position, disk_size, direction):
    """
    C-SCAN (Circular SCAN) Disk Scheduling Algorithm
    :param requests: List of disk requests (cylinder numbers)
    :param head_position: Initial position of the disk head
    :param disk_size: The size of the disk (total number of cylinders)
    :param direction: The direction of movement ('right' or 'left')
    :return: The sequence of head movements and the total head movement
    """
    requests = sorted(requests)
    
    # Split requests into two lists: one to the right of the head and one to the left
    right = [r for r in requests if r >= head_position]
    left = [r for r in requests if r < head_position]
    right.sort()
    left.sort(reverse=True)

    # If moving right first
    if direction == 'right':
        sequence = [head_position] + right + [disk_size - 1] + left
    # If moving left first
    else:
        sequence = [head_position] + left + [0] + right
    
    # Calculate the total head movement
    total_head_movement = sum(abs(sequence[i] - sequence[i + 1]) for i in range(len(sequence) - 1))

    return sequence, total_head_movement
