
# Usage Guide

## Basic Usage
Run the simulator with default parameters:
```bash
python -m disk_scheduling_simulator
```
### Command Line Options
The simulator can be configured through the GUI, but you can also prepare input files:

### Request File Format
Create a text file with space-separated or newline-separated cylinder numbers:

```csv
98 183 37 122 14 124 65 67
```
### GUI Controls

- **Disk Size:** Set the total number of cylinders (default: 200)
- **nitial Head Position:** Set starting position of disk head
- **Requests:** Enter comma-separated cylinder requests
- **Algorithm:** Select from the six implemented algorithms
- **Direction:** Choose direction for SCAN and LOOK algorithms
- **Random Requests:** Generate random valid requests
- **Load from File:** Load requests from a text file

### Educational Use
The simulator is designed for teaching operating system concepts. Instructors can:

- Demonstrate different scheduling algorithms
- Compare total head movement across algorithms
- Visualize head movement patterns
- Discuss algorithm advantages and disadvantages



