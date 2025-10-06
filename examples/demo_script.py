
"""
Demo script showing how to use the disk scheduling algorithms programmatically.
"""

from src.disk_scheduling_simulator.algorithms import DiskScheduler

def main():
    # Initialize scheduler
    scheduler = DiskScheduler(disk_size=200, initial_head=50)
    
    # Set requests
    requests = [98, 183, 37, 122, 14, 124, 65, 67]
    
    # Run all algorithms
    algorithms = ['FCFS', 'SSTF', 'SCAN', 'C-SCAN', 'LOOK', 'C-LOOK']
    
    print("Disk Scheduling Algorithms Comparison")
    print("=" * 50)
    print(f"Initial Head: {scheduler.initial_head}")
    print(f"Requests: {requests}")
    print("-" * 50)
    
    for algo in algorithms:
        sequence, total_movement = scheduler.run_algorithm(algo, requests, direction='Right')
        print(f"{algo:8}: Total Movement = {total_movement:3} | Sequence: {sequence}")
    
    print("=" * 50)

if __name__ == "__main__":
    main()