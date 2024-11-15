# clook.py

def clook(requests, head_position):
    """
    C-LOOK Disk Scheduling Algorithm (Circular LOOK)
    :param requests: List of disk requests (cylinder numbers)
    :param head_position: Initial position of the disk head
    :return: The sequence of head movements and the total head movement
    """
    requests = sorted(requests)

    # Separate requests into those left and right of the current head position
    left = [r for r in requests if r < head_position]
    right = [r for r in requests if r > head_position]

    # Reverse the left list so that we process it in decreasing order
    left.sort(reverse=True)
    right.sort()

    # Sequence of head movements
    sequence = [head_position]

    # Process requests in the right direction first
    sequence.extend(right)
    # Jump to the beginning (circular move) and process the left requests
    sequence.extend(left)

    total_head_movement = sum(abs(sequence[i] - sequence[i + 1]) for i in range(len(sequence) - 1))

    return sequence, total_head_movement
