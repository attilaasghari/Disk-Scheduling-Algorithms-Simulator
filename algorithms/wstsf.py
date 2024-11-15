def wstsf(requests, head_position, weights, disk_size=None):
    """
    Weighted Shortest Seek Time First (WSTSF) Disk Scheduling Algorithm.
    :param requests: List of disk requests (cylinder numbers).
    :param head_position: Initial position of the disk head.
    :param weights: List of weights for each request.
    :param disk_size: Optional size of the disk (total number of cylinders).
    :return: The sequence of head movements and the total head movement.
    """
    # Optional validation for disk size
    if disk_size is not None:
        assert all(0 <= req < disk_size for req in requests), "Request out of disk size bounds."

    # Combine requests and weights into a list of tuples (request, weight)
    weighted_requests = list(zip(requests, weights))
    
    sequence = []
    total_head_movement = 0

    while weighted_requests:
        # Calculate the weighted seek time (distance * weight)
        distances = [(abs(req - head_position), weight, req) for req, weight in weighted_requests]
        
        # Sort by the smallest weighted distance
        distances.sort(key=lambda x: x[0] * x[1])
        
        # Choose the request with the minimum weighted distance
        min_distance, weight, request = distances[0]
        weighted_requests.remove((request, weight))
        
        # Add to the sequence and calculate total head movement
        sequence.append(request)
        total_head_movement += min_distance
        head_position = request  # Move the head to the chosen request

    
    return sequence, total_head_movement

