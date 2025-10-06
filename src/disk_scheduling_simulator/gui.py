"""
GUI implementation for the Disk Scheduling Simulator.
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
import sys
import os
from .algorithms import DiskScheduler

def run_simulator():
    """Launch the disk scheduling simulator GUI."""
    root = tk.Tk()
    app = DiskSchedulingGUI(root)
    root.mainloop()

class DiskSchedulingGUI:
    """Main GUI class for the disk scheduling simulator."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Disk Scheduling Algorithms Simulator")
        self.root.geometry("1200x800")
        self.root.configure(bg="#f0f0f0")
        self.set_window_icon()
        
        # Default parameters
        self.disk_size = 200
        self.initial_head = 50
        self.requests = [98, 183, 37, 122, 14, 124, 65, 67]
        
        # Create GUI
        self.create_widgets()
        self.update_request_list()

    def set_window_icon(self):
        """Set the window icon if icon file is available."""
        try:
            if getattr(sys, 'frozen', False):
                # Running as compiled executable
                icon_path = os.path.join(os.path.dirname(sys.executable), 'icon.ico')
            else:
                # Running as script
                icon_path = os.path.join(os.path.dirname(__file__), '..', 'icon.ico')

            if os.path.exists(icon_path):
                self.root.iconbitmap(icon_path)
        except Exception:
            # Icon not available or not supported on this platform
            pass
    
    def create_widgets(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        
        # Left panel - Controls
        control_frame = ttk.LabelFrame(main_frame, text="Simulation Controls", padding="10")
        control_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(0, 10))
        control_frame.columnconfigure(1, weight=1)
        
        # Disk size
        ttk.Label(control_frame, text="Disk Size (cylinders):").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.disk_size_var = tk.IntVar(value=self.disk_size)
        disk_size_entry = ttk.Entry(control_frame, textvariable=self.disk_size_var, width=10)
        disk_size_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5)
        
        # Initial head position
        ttk.Label(control_frame, text="Initial Head Position:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.head_pos_var = tk.IntVar(value=self.initial_head)
        head_pos_entry = ttk.Entry(control_frame, textvariable=self.head_pos_var, width=10)
        head_pos_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5)
        
        # Requests input
        ttk.Label(control_frame, text="Disk Requests (comma separated):").grid(row=2, column=0, columnspan=2, sticky=tk.W, pady=(10, 5))
        self.requests_var = tk.StringVar(value=", ".join(map(str, self.requests)))
        requests_entry = ttk.Entry(control_frame, textvariable=self.requests_var, width=30)
        requests_entry.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        # Request generation buttons
        gen_frame = ttk.Frame(control_frame)
        gen_frame.grid(row=4, column=0, columnspan=2, pady=10)
        ttk.Button(gen_frame, text="Random Requests", command=self.generate_random_requests).pack(side=tk.LEFT, padx=5)
        ttk.Button(gen_frame, text="Load from File", command=self.load_requests_from_file).pack(side=tk.LEFT, padx=5)
        
        # Algorithm selection
        ttk.Label(control_frame, text="Select Algorithm:").grid(row=5, column=0, columnspan=2, sticky=tk.W, pady=(10, 5))
        self.algorithm_var = tk.StringVar(value="FCFS")
        algorithm_combo = ttk.Combobox(control_frame, textvariable=self.algorithm_var, 
                                      values=["FCFS", "SSTF", "SCAN", "C-SCAN", "LOOK", "C-LOOK"], state="readonly")
        algorithm_combo.grid(row=6, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        # Direction for SCAN and LOOK algorithms
        self.direction_var = tk.StringVar(value="Right")
        direction_frame = ttk.Frame(control_frame)
        direction_frame.grid(row=7, column=0, columnspan=2, pady=5)
        ttk.Label(direction_frame, text="Direction:").pack(side=tk.LEFT)
        ttk.Radiobutton(direction_frame, text="Right", variable=self.direction_var, value="Right").pack(side=tk.LEFT, padx=5)
        ttk.Radiobutton(direction_frame, text="Left", variable=self.direction_var, value="Left").pack(side=tk.LEFT, padx=5)
        
        # Run simulation button
        ttk.Button(control_frame, text="Run Simulation", command=self.run_simulation).grid(row=8, column=0, columnspan=2, pady=15)
        
        # Results frame
        results_frame = ttk.LabelFrame(main_frame, text="Results", padding="10")
        results_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(0, 10), pady=(10, 0))
        results_frame.columnconfigure(0, weight=1)
        
        # Results text
        self.results_text = tk.Text(results_frame, height=8, wrap=tk.WORD)
        self.results_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        results_scroll = ttk.Scrollbar(results_frame, orient=tk.VERTICAL, command=self.results_text.yview)
        results_scroll.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.results_text.configure(yscrollcommand=results_scroll.set)
        
        # Right panel - Visualization
        viz_frame = ttk.LabelFrame(main_frame, text="Visualization", padding="10")
        viz_frame.grid(row=0, column=1, rowspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        viz_frame.columnconfigure(0, weight=1)
        viz_frame.rowconfigure(0, weight=1)
        
        # Matplotlib figure
        self.fig, self.ax = plt.subplots(figsize=(8, 6))
        self.canvas = FigureCanvasTkAgg(self.fig, viz_frame)
        self.canvas.get_tk_widget().grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(0, weight=1)
        main_frame.rowconfigure(1, weight=1)
        control_frame.rowconfigure(4, weight=1)
        results_frame.rowconfigure(0, weight=1)
        viz_frame.rowconfigure(0, weight=1)
    
    def update_request_list(self):
        """Update the request list from the entry field"""
        try:
            requests_str = self.requests_var.get().strip()
            if requests_str:
                self.requests = [int(x.strip()) for x in requests_str.split(",") if x.strip()]
            else:
                self.requests = []
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid integers for disk requests.")
            self.requests = [98, 183, 37, 122, 14, 124, 65, 67]
            self.requests_var.set(", ".join(map(str, self.requests)))
    
    def generate_random_requests(self):
        """Generate random disk requests"""
        self.disk_size = self.disk_size_var.get()
        num_requests = random.randint(5, 15)
        self.requests = [random.randint(0, self.disk_size - 1) for _ in range(num_requests)]
        self.requests_var.set(", ".join(map(str, self.requests)))
    
    def load_requests_from_file(self):
        """Load disk requests from a file"""
        file_path = filedialog.askopenfilename(
            title="Select Request File",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    content = file.read().strip()
                    # Handle both space and comma separated values
                    if ',' in content:
                        self.requests = [int(x) for x in content.split(',') if x.strip().isdigit()]
                    else:
                        self.requests = [int(x) for x in content.split() if x.strip().isdigit()]
                    self.requests_var.set(", ".join(map(str, self.requests)))
            except Exception as e:
                messagebox.showerror("File Error", f"Error reading file: {str(e)}")
    
    def run_simulation(self):
        """Run the selected disk scheduling algorithm"""
        # Update parameters
        self.disk_size = self.disk_size_var.get()
        self.initial_head = self.head_pos_var.get()
        self.update_request_list()
        
        # Validate inputs
        if not self.requests:
            messagebox.showerror("Input Error", "Please provide at least one disk request.")
            return
        
        if self.initial_head < 0 or self.initial_head >= self.disk_size:
            messagebox.showerror("Input Error", f"Initial head position must be between 0 and {self.disk_size - 1}.")
            return
        
        for req in self.requests:
            if req < 0 or req >= self.disk_size:
                messagebox.showerror("Input Error", f"All requests must be between 0 and {self.disk_size - 1}.")
                return
        
        # Get selected algorithm
        algorithm = self.algorithm_var.get()
        direction = self.direction_var.get()
        
        # Run the algorithm
        scheduler = DiskScheduler(self.disk_size, self.initial_head)
        sequence, total_movement = scheduler.run_algorithm(algorithm, self.requests, direction)
        
        # Display results
        self.display_results(algorithm, sequence, total_movement)
        self.visualize_sequence(sequence)
    
    def display_results(self, algorithm, sequence, total_movement):
        """Display simulation results in the text widget"""
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.END, f"Algorithm: {algorithm}\n")
        self.results_text.insert(tk.END, f"Initial Head Position: {self.initial_head}\n")
        self.results_text.insert(tk.END, f"Request Sequence: {self.requests}\n")
        self.results_text.insert(tk.END, f"Head Movement Sequence: {sequence}\n")
        self.results_text.insert(tk.END, f"Total Head Movement: {total_movement} cylinders\n")
        
        # Add algorithm description
        descriptions = {
            "FCFS": "First-Come, First-Served: Processes requests in the order they arrive.",
            "SSTF": "Shortest Seek Time First: Always chooses the request closest to the current head position.",
            "SCAN": "Elevator Algorithm: Moves head in one direction servicing requests until the end, then reverses.",
            "C-SCAN": "Circular SCAN: Moves head in one direction servicing requests, then jumps to the beginning and continues.",
            "LOOK": "Similar to SCAN but doesn't go all the way to the end; reverses when no more requests in current direction.",
            "C-LOOK": "Circular LOOK: Similar to C-SCAN but doesn't go all the way to the end; jumps to the first request in the other direction."
        }
        self.results_text.insert(tk.END, f"\nDescription: {descriptions[algorithm]}")
    
    def visualize_sequence(self, sequence):
        """Visualize the head movement sequence"""
        self.ax.clear()
        
        # Create x-axis (time steps) and y-axis (cylinder positions)
        x = list(range(len(sequence)))
        y = sequence
        
        # Plot the movement
        self.ax.plot(x, y, 'bo-', linewidth=2, markersize=8)
        self.ax.set_xlabel('Time Step')
        self.ax.set_ylabel('Cylinder Position')
        self.ax.set_title('Disk Head Movement Sequence')
        self.ax.grid(True, linestyle='--', alpha=0.7)
        self.ax.set_ylim(-5, self.disk_size + 5)
        
        # Add disk boundaries
        self.ax.axhline(y=0, color='r', linestyle='--', alpha=0.5)
        self.ax.axhline(y=self.disk_size-1, color='r', linestyle='--', alpha=0.5)
        self.ax.text(-0.5, -3, '0', fontsize=9, ha='center')
        self.ax.text(-0.5, self.disk_size+2, f'{self.disk_size-1}', fontsize=9, ha='center')
        
        # Annotate points
        for i, (xi, yi) in enumerate(zip(x, y)):
            self.ax.annotate(str(yi), (xi, yi), textcoords="offset points", 
                            xytext=(0,10), ha='center', fontsize=9)
        
        self.canvas.draw()