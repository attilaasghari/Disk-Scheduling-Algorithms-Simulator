# Disk Scheduling Algorithms

This repository contains implementations of various **Disk Scheduling Algorithms**. These algorithms are used to determine the order in which disk I/O requests are processed. The goal of these algorithms is to optimize the movement of the disk head, reducing the total time or distance the head has to travel. 

The algorithms implemented in this repository include:

- **FCFS (First-Come, First-Served)**
- **SSTF (Shortest Seek Time First)**
- **SCAN (Elevator)**
- **C-SCAN (Circular SCAN)**
- **LOOK**
- **C-LOOK (Circular LOOK)**
- **Priority Scheduling**
- **WSTSF (Weighted Shortest Seek Time First)**

Each algorithm has its own unique approach to handling disk I/O requests and is useful in different scenarios.

## Algorithms Overview

### 1. **FCFS (First-Come, First-Served)**
   - The simplest disk scheduling algorithm where requests are processed in the order they arrive.

### 2. **SSTF (Shortest Seek Time First)**
   - This algorithm selects the disk request that is closest to the current head position, minimizing the seek time.

### 3. **SCAN (Elevator)**
   - The disk arm moves in one direction, serving requests in its path until it reaches the end, then reverses direction.

### 4. **C-SCAN (Circular SCAN)**
   - A variant of SCAN where, after reaching the end of the disk, the head returns to the beginning and continues serving requests.

### 5. **LOOK**
   - Similar to SCAN, but the head only goes as far as the last request in the current direction, reversing direction after reaching the end of the requests.

### 6. **C-LOOK (Circular LOOK)**
   - A variant of LOOK where the head returns to the farthest request after reaching the last request in the current direction.

### 7. **Priority Scheduling**
   - Requests are served based on their priority. Requests with higher priority (lower priority number) are served first.

### 8. **WSTSF (Weighted Shortest Seek Time First)**
   - A modified version of SSTF that considers the weight of each request. The seek time is weighted by a given priority, allowing more important requests to be processed sooner.

## Features

- Implementation of disk scheduling algorithms using Python.
- Ability to visualize the disk head movement for each algorithm.
- Option to specify weights for requests in WSTSF.
- Easy-to-use functions that take disk requests and initial head position as inputs.

## Installation

To use the disk scheduling algorithms, you need to have Python installed on your system. You can clone this repository and install the necessary dependencies:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/disk-scheduling-algorithms.git
   cd disk-scheduling-algorithms
   ```

2. **Install the required dependencies:**
   
    You will need the `matplotlib` library for plotting the disk head movement. You can install it via `pip`:

    ```bash 
    pip install matplotlib
    ```

## Usage
### Example:
To use one of the algorithms, simply import the function and provide the disk requests and the initial head position.

```bash
from fcfs import fcfs
from sstf import sstf
from scan import scan

# Example disk requests and initial head position
requests = [98, 183, 37, 122, 14, 124, 65, 67]
head_position = 53

# Using FCFS
sequence, total_movement = fcfs(requests, head_position)
print(f"FCFS Sequence: {sequence}, Total Head Movement: {total_movement}")

# Using SSTF
sequence, total_movement = sstf(requests, head_position)
print(f"SSTF Sequence: {sequence}, Total Head Movement: {total_movement}")

# Using SCAN (direction 'right')
sequence, total_movement = scan(requests, head_position, direction='right', disk_size=200)
print(f"SCAN Sequence: {sequence}, Total Head Movement: {total_movement}")
```
You can replace `fcfs`, `sstf`, and `scan` with any other algorithm function like `look`, `cscan`, or `priority_scheduling` as needed.

### Visualizing Disk Head Movement

Each algorithm can also plot the sequence of disk head movements using `matplotlib`. Here’s an example for `SSTF`:

```bash 
from visualization import plot_disk_head_movement
sequence, _ = sstf(requests, head_position)
plot_disk_head_movement(sequence, title="SSTF Disk Scheduling")

```

## Contributing
Contributions are welcome! If you'd like to contribute to the project, feel free to fork the repository, make changes, and submit a pull request. If you encounter any issues or have suggestions for improvements, please open an issue.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


#### Created by Attila Asghari




