# Disk Scheduling Algorithms Implemented

This document explains the six disk scheduling algorithms implemented in the simulator.

## FCFS (First-Come, First-Served)
Processes requests in the exact order they arrive. Simple but often inefficient as it doesn't consider the current head position.

## SSTF (Shortest Seek Time First)
Always selects the request closest to the current head position. Reduces average seek time but can cause starvation for requests far from the head.

## SCAN (Elevator Algorithm)
Moves the head in one direction servicing all requests until it reaches the end of the disk, then reverses direction. Provides fair service to all requests.

## C-SCAN (Circular SCAN)
Similar to SCAN but when the head reaches the end, it immediately returns to the beginning without servicing requests on the return trip, then continues in the same direction.

## LOOK
An optimized version of SCAN that doesn't go all the way to the end of the disk. Instead, it reverses direction when there are no more requests in the current direction.

## C-LOOK
An optimized version of C-SCAN that doesn't go all the way to the end. When no more requests exist in the current direction, it jumps to the farthest request in the opposite direction.