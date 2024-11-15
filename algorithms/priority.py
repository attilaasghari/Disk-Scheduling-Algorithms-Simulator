def priority_scheduling(requests, priorities):
    """
    Implements the Priority Scheduling algorithm for disk requests.

    Args:
        requests (list of int): The list of disk requests.
        priorities (list of int): The priority levels of each request (lower value = higher priority).

    Returns:
        tuple: A tuple containing the processed sequence of requests and the total head movement.
    """
    if len(requests) != len(priorities):
        raise ValueError("The number of priorities must match the number of requests.")

    # Combine requests with their priorities and sort by priority (ascending order)
    combined = sorted(zip(priorities, requests), key=lambda x: x[0])
    sorted_requests = [req for _, req in combined]

    return sorted_requests
