# visualization.py

import matplotlib.pyplot as plt
import numpy as np

def plot_disk_head_movement(sequence, title="Disk Scheduling", color="blue"):
    """
    Plots the disk head movement on a graph.
    :param sequence: The sequence of disk head positions
    :param title: Title of the graph
    """
    plt.figure(figsize=(10, 5))
    x = np.arange(len(sequence))
    y = sequence
    plt.plot(x, y, marker="o", color=color, label="Disk Head Movement")
    plt.annotate("Start", (x[0], y[0]), textcoords="offset points", xytext=(0,10), ha='center')
    plt.annotate("End", (x[-1], y[-1]), textcoords="offset points", xytext=(0,-15), ha='center')
    plt.title(title)
    plt.xlabel("Request Order")
    plt.ylabel("Cylinder Number")
    plt.grid(True)
    plt.legend()
    plt.show()
