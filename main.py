import tkinter as tk
from tkinter import ttk
import random
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

class DiskSchedulingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Disk Scheduling Algorithms Simulator")
        
        # Input Fields
        self.init_pos_label = ttk.Label(root, text="Initial Position:")
        self.init_pos_entry = ttk.Entry(root)
        
        self.requests_label = ttk.Label(root, text="Requests (comma-separated):")
        self.requests_entry = ttk.Entry(root, width=40)
        
        self.algorithm_label = ttk.Label(root, text="Algorithm:")
        self.algorithm_var = tk.StringVar()
        self.algorithm_combobox = ttk.Combobox(root, textvariable=self.algorithm_var,
                                             values=["FCFS", "SSTF", "SCAN", "C-SCAN", "LOOK", "C-LOOK"])
        
        # Buttons
        self.simulate_btn = ttk.Button(root, text="Simulate", command=self.simulate)
        self.random_btn = ttk.Button(root, text="Generate Random", command=self.generate_random)
        self.clear_btn = ttk.Button(root, text="Clear", command=self.clear)
        
        # Results Display
        self.result_label = ttk.Label(root, text="Results will be shown here")
        self.figure = plt.figure(figsize=(6, 4))
        self.canvas = FigureCanvasTkAgg(self.figure, master=root)
        
        # Layout
        self.init_pos_label.grid(row=0, column=0, padx=5, pady=5)
        self.init_pos_entry.grid(row=0, column=1, padx=5, pady=5)
        
        self.requests_label.grid(row=1, column=0, padx=5, pady=5)
        self.requests_entry.grid(row=1, column=1, padx=5, pady=5)
        
        self.algorithm_label.grid(row=2, column=0, padx=5, pady=5)
        self.algorithm_combobox.grid(row=2, column=1, padx=5, pady=5)
        self.algorithm_combobox.current(0)
        
        self.simulate_btn.grid(row=3, column=0, padx=5, pady=5)
        self.random_btn.grid(row=3, column=1, padx=5, pady=5)
        self.clear_btn.grid(row=3, column=2, padx=5, pady=5)
        
        self.result_label.grid(row=4, column=0, columnspan=3, padx=5, pady=5)
        self.canvas.get_tk_widget().grid(row=5, column=0, columnspan=3, padx=5, pady=5)

    def generate_random(self):
        initial = random.randint(0, 200)
        requests = [random.randint(0, 200) for _ in range(10)]
        self.init_pos_entry.delete(0, tk.END)
        self.init_pos_entry.insert(0, str(initial))
        self.requests_entry.delete(0, tk.END)
        self.requests_entry.insert(0, ",".join(map(str, requests)))

    def clear(self):
        self.init_pos_entry.delete(0, tk.END)
        self.requests_entry.delete(0, tk.END)
        self.result_label.config(text="Results will be shown here")
        self.figure.clear()
        self.canvas.draw()

    def fcfs(self, initial, requests):
        sequence = [initial] + requests
        total_movement = abs(sequence[0] - sequence[1])
        for i in range(1, len(sequence)-1):
            total_movement += abs(sequence[i] - sequence[i+1])
        return total_movement, sequence

    def sstf(self, initial, requests):
        sequence = [initial]
        requests = sorted(requests.copy())
        current = initial
        total_movement = 0

        while requests:
            closest = min(requests, key=lambda x: abs(x - current))
            total_movement += abs(closest - current)
            current = closest
            sequence.append(current)
            requests.remove(current)

        return total_movement, sequence

    def scan(self, initial, requests, disk_size=200):
        requests = sorted(requests)
        sequence = [initial]
        total_movement = 0
        current = initial

        left = [r for r in requests if r <= current]
        right = [r for r in requests if r > current]

        right.sort()
        left.sort(reverse=True)

        # Service right side
        for r in right:
            total_movement += abs(r - current)
            current = r
            sequence.append(current)

        # Only go to disk end if size is specified (SCAN mode)
        if disk_size is not None:
            if current != disk_size:
                total_movement += abs(disk_size - current)
                current = disk_size
                sequence.append(current)

        # Service left side
        for r in left:
            total_movement += abs(r - current)
            current = r
            sequence.append(current)

        return total_movement, sequence

    def c_scan(self, initial, requests, disk_size=200):
        requests = sorted(requests)
        sequence = [initial]
        total_movement = 0
        current = initial

        right = [r for r in requests if r >= current]
        left = [r for r in requests if r < current]

        for r in right:
            total_movement += abs(r - current)
            current = r
            sequence.append(current)

        if current != disk_size:
            total_movement += abs(disk_size - current)
            current = disk_size
            sequence.append(current)

        # Jump to start
        if left:
            total_movement += disk_size
            current = 0
            sequence.append(0)

        for r in left:
            total_movement += abs(r - current)
            current = r
            sequence.append(current)

        return total_movement, sequence

    def look(self, initial, requests):
        # Call scan with disk_size=None to prevent end-of-disk movement
        return self.scan(initial, requests, disk_size=None)

    def c_look(self, initial, requests):
        requests = sorted(requests)
        sequence = [initial]
        total_movement = 0
        current = initial

        right = [r for r in requests if r >= current]
        left = [r for r in requests if r < current]

        for r in right:
            total_movement += abs(r - current)
            current = r
            sequence.append(current)

        for r in left:
            total_movement += abs(r - current)
            current = r
            sequence.append(current)

        return total_movement, sequence
    
    # Simulation and plotting will go here
    def simulate(self):
        try:
            initial = int(self.init_pos_entry.get())
            requests = list(map(int, self.requests_entry.get().split(',')))
            algorithm = self.algorithm_var.get()
        except ValueError:
            self.result_label.config(text="Invalid input! Please enter numbers only")
            return

        algorithm_map = {
            "FCFS": self.fcfs,
            "SSTF": self.sstf,
            "SCAN": self.scan,
            "C-SCAN": self.c_scan,
            "LOOK": self.look,
            "C-LOOK": self.c_look
        }

        total_movement, sequence = algorithm_map[algorithm](initial, requests)

        # Update results
        result_text = f"Algorithm: {algorithm}\nTotal Head Movement: {total_movement}\nSequence: {sequence}"
        self.result_label.config(text=result_text)

        # Plotting
        self.figure.clear()
        ax = self.figure.add_subplot(111)

        # Plot sequence with arrows
        x = list(range(len(sequence)))
        y = sequence
        ax.plot(x, y, 'b-o', markersize=8)

        # Add labels and title
        ax.set_title(f"{algorithm} Disk Scheduling")
        ax.set_xlabel("Step")
        ax.set_ylabel("Cylinder Number")
        ax.grid(True)

        # Annotate points
        for i, (xi, yi) in enumerate(zip(x, y)):
            ax.annotate(str(yi), (xi, yi), textcoords="offset points", xytext=(0,10), ha='center')

        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = DiskSchedulingApp(root)
    root.mainloop()