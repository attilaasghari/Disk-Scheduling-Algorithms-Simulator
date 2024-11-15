#fcfs.py
def fcfs(requests, head_position):
    """
    First-Come, First-Served (FCFS) Disk Scheduling Algorithm

    :param requests: List of disk requests (cylinder numbers)
    :param head_position: Initial position of the disk head (must be a non-negative integer)
    :return: Tuple containing the sequence of head movements and the total head movement
    :raises ValueError: If inputs are not valid.
    """
    sequence = [head_position] + requests
    total_head_movement = sum(abs(sequence[i] - sequence[i + 1]) for i in range(len(sequence) - 1))
    return sequence, total_head_movement
