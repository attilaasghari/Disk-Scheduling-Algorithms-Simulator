# look.py

def look(requests, head_position, direction):
    """
    LOOK Disk Scheduling Algorithm
    :param requests: List of disk requests (cylinder numbers)
    :param head_position: Initial position of the disk head
    :param direction: Direction of the head movement ('left' or 'right')
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

    if direction == 'right':
        sequence.extend(right)  # Move right first
        sequence.extend(left)   # Then move left
    elif direction == 'left':
        sequence.extend(left)   # Move left first
        sequence.extend(right)  # Then move right

    total_head_movement = sum(abs(sequence[i] - sequence[i + 1]) for i in range(len(sequence) - 1))

    return sequence, total_head_movement
