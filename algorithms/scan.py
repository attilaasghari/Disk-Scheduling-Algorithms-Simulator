def scan(requests, head_position, direction, disk_size):
    """
    SCAN (Elevator) Disk Scheduling Algorithm
    :param requests: List of disk requests (cylinder numbers)
    :param head_position: Initial position of the disk head
    :param direction: Direction the elevator head moves ('left' or 'right')
    :param disk_size: The size of the disk (total number of cylinders)
    :return: The sequence of head movements and the total head movement
    """
    requests = sorted(requests)
    
    # Adding the boundary condition (disk size) to the logic
    if direction == "right":
        # Move towards the right end of the disk
        right = [r for r in requests if r >= head_position]
        left = [r for r in requests if r < head_position]
        right.sort()
        left.sort(reverse=True)

        # Add the last position of the head movement if it reaches the end
        if right:
            sequence = [head_position] + right + [disk_size - 1] + left
        else:
            sequence = [head_position] + [disk_size - 1] + left
    elif direction == "left":
        # Move towards the left end of the disk
        left = [r for r in requests if r <= head_position]
        right = [r for r in requests if r > head_position]
        left.sort(reverse=True)
        right.sort()

        # Add the first position of the head movement if it reaches the start
        if left:
            sequence = [head_position] + left + [0] + right
        else:
            sequence = [head_position] + [0] + right
    
    # Calculate total head movement
    total_head_movement = sum(abs(sequence[i] - sequence[i + 1]) for i in range(len(sequence) - 1))
    
    return sequence, total_head_movement
