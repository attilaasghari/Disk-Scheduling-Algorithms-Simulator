import tkinter as tk
from tkinter import messagebox
from algorithms.fcfs import fcfs  # Importing the FCFS algorithm
from algorithms.sstf import sstf  # Importing the SSTF algorithm
from algorithms.scan import scan  # Importing the SCAN algorithm
from algorithms.cscan import cscan  # Importing the C-SCAN algorithm
from algorithms.look import look  # Importing the LOOK algorithm
from algorithms.clook import clook  # Importing the C-LOOK algorithm
from algorithms.wstsf import wstsf  # Importing the WSTSF algorithm
from algorithms.priority import priority_scheduling  # Importing the Priority Scheduling algorithm
from utils.visualization import plot_disk_head_movement  # Importing the plotting utility

class DiskSchedulingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Disk Scheduling Algorithms")
        self.root.geometry("600x600")  # Adjusted for disk size input field

        # Initialize GUI Components
        self.create_widgets()

    def create_widgets(self):
        # Set a dark background color for the entire interface
        self.root.configure(bg="#1e1e1e")
    
        # Title with LHC-inspired futuristic font and color
        title = tk.Label(self.root, text="Disk Scheduling Simulator", fg="#00c8ff", bg="#1e1e1e", font=("Helvetica", 18, "bold"))
        title.pack(pady=20)
    
        # Create a "radar-like" frame for input fields with dark background
        input_frame = tk.Frame(self.root, bg="#1e1e1e")
        input_frame.pack(pady=30)
    
        # Add Disk Requests Input with cyan accents
        tk.Label(input_frame, text="Disk Requests (comma-separated):", fg="#00c8ff", bg="#1e1e1e", font=("Helvetica", 12)).grid(row=0, column=0, pady=5, sticky="w")
        self.requests_entry = tk.Entry(input_frame, width=40, fg="#ffffff", bg="#2e2e2e", insertbackground="white", font=("Helvetica", 10))
        self.requests_entry.grid(row=0, column=1, padx=10)
    
        # Add Initial Head Position Input with neon blue color
        tk.Label(input_frame, text="Initial Head Position:", fg="#00c8ff", bg="#1e1e1e", font=("Helvetica", 12)).grid(row=1, column=0, pady=5, sticky="w")
        self.head_entry = tk.Entry(input_frame, width=40, fg="#ffffff", bg="#2e2e2e", insertbackground="white", font=("Helvetica", 10))
        self.head_entry.grid(row=1, column=1, padx=10)
    
        # Add Disk Size Input with appropriate neon accents
        tk.Label(input_frame, text="Disk Size:", fg="#00c8ff", bg="#1e1e1e", font=("Helvetica", 12)).grid(row=2, column=0, pady=5, sticky="w")
        self.disk_size_entry = tk.Entry(input_frame, width=40, fg="#ffffff", bg="#2e2e2e", insertbackground="white", font=("Helvetica", 10))
        self.disk_size_entry.grid(row=2, column=1, padx=10)
    
        # Dropdown for Algorithm Selection with accent highlight color
        tk.Label(input_frame, text="Algorithm:", fg="#00c8ff", bg="#1e1e1e", font=("Helvetica", 12)).grid(row=3, column=0, pady=5, sticky="w")
        self.algorithm_var = tk.StringVar(value="FCFS")
        self.algorithm_menu = tk.OptionMenu(input_frame, self.algorithm_var, "FCFS", "SSTF", "SCAN", "C-SCAN", "LOOK", "C-LOOK", "WSTSF", "Priority")
        self.algorithm_menu.config(bg="#2e2e2e", fg="#ffffff", activebackground="#00c8ff", font=("Helvetica", 10))
        self.algorithm_menu.grid(row=3, column=1, padx=10, sticky="w")
    
        # Add Direction Dropdown for SCAN-like algorithms with neon accents
        tk.Label(input_frame, text="Direction (SCAN/C-SCAN/LOOK):", fg="#00c8ff", bg="#1e1e1e", font=("Helvetica", 12)).grid(row=4, column=0, pady=5, sticky="w")
        self.direction_var = tk.StringVar(value="right")
        self.direction_menu = tk.OptionMenu(input_frame, self.direction_var, "right", "left")
        self.direction_menu.config(bg="#2e2e2e", fg="#ffffff", activebackground="#00c8ff", font=("Helvetica", 10))
        self.direction_menu.grid(row=4, column=1, padx=10, sticky="w")
    
        # Add Weights Input for WSTSF with neon green accents
        tk.Label(input_frame, text="Weights (comma-separated):", fg="#6aff00", bg="#1e1e1e", font=("Helvetica", 12)).grid(row=5, column=0, pady=5, sticky="w")
        self.weights_entry = tk.Entry(input_frame, width=40, fg="#ffffff", bg="#2e2e2e", insertbackground="white", font=("Helvetica", 10))
        self.weights_entry.grid(row=5, column=1, padx=10)
    
        # Add Priorities Input for Priority Scheduling with a dark blue shade
        tk.Label(input_frame, text="Priorities (comma-separated):", fg="#1fb1fc", bg="#1e1e1e", font=("Helvetica", 12)).grid(row=6, column=0, pady=5, sticky="w")
        self.priorities_entry = tk.Entry(input_frame, width=40, fg="#ffffff", bg="#2e2e2e", insertbackground="white", font=("Helvetica", 10))
        self.priorities_entry.grid(row=6, column=1, padx=10)
    
        # Add Run Button with glowing cyan effect
        self.run_button = tk.Button(self.root, text="Run Simulation", command=self.run_algorithm, bg="#00c8ff", fg="#1e1e1e", font=("Helvetica", 12, "bold"), activebackground="#2e2e2e")
        self.run_button.pack(pady=25)
    
        # Output Text Area for Results with dark theme and contrasting colors
        self.output_text = tk.Text(self.root, height=10, width=60, bg="#2e2e2e", fg="#ffffff", font=("Courier", 10), state="disabled", wrap="word", insertbackground="white")
        self.output_text.pack(pady=20)


    def run_algorithm(self):
        # Get input data
        requests = self.requests_entry.get()
        head_position = self.head_entry.get()
        disk_size = self.disk_size_entry.get()
    
        try:
            requests = [int(x) for x in requests.split(",")]
            if self.algorithm_var.get() != "Priority":  # Only parse head position for algorithms that need it
                head_position = int(head_position)
            else:
                head_position = None
            disk_size = int(disk_size) if disk_size else None
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numeric values.")
            return
    
        algorithm = self.algorithm_var.get()
        if algorithm == "FCFS":
            self.run_fcfs(requests, head_position)
        elif algorithm == "SSTF":
            self.run_sstf(requests, head_position)
        elif algorithm == "SCAN":
            if not disk_size:
                messagebox.showerror("Input Error", "Disk size is required for SCAN algorithm.")
                return
            self.run_scan(requests, head_position, disk_size)
        elif algorithm == "C-SCAN":
            if not disk_size:
                messagebox.showerror("Input Error", "Disk size is required for C-SCAN algorithm.")
                return
            self.run_cscan(requests, head_position, disk_size)
        elif algorithm == "LOOK":
            self.run_look(requests, head_position, disk_size)
        elif algorithm == "C-LOOK":
            self.run_clook(requests, head_position)
        elif algorithm == "WSTSF":
            self.run_wstsf(requests, head_position, disk_size)
        elif algorithm == "Priority":
            self.run_priority(requests)
    
        else:
            messagebox.showerror("Algorithm Not Implemented", "This algorithm is not yet implemented.")


    def run_fcfs(self, requests, head_position):
        sequence, total_head_movement = fcfs(requests, head_position)
        
        # Display results
        result_text = f"Algorithm: FCFS\n"
        result_text += f"Request Sequence: {sequence}\n"
        result_text += f"Total Head Movement: {total_head_movement} cylinders\n"
        
        self.output_text.config(state="normal")
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, result_text)
        self.output_text.config(state="disabled")
        
        # Plot timing chart
        plot_disk_head_movement(sequence, "FCFS Disk Scheduling")
    
    def run_sstf(self, requests, head_position):
        sequence, total_head_movement = sstf(requests, head_position)
        
        # Display results
        result_text = f"Algorithm: SSTF\n"
        result_text += f"Request Sequence: {sequence}\n"
        result_text += f"Total Head Movement: {total_head_movement} cylinders\n"
        
        self.output_text.config(state="normal")
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, result_text)
        self.output_text.config(state="disabled")
        
        # Plot timing chart
        plot_disk_head_movement(sequence, "SSTF Disk Scheduling")

    def run_scan(self, requests, head_position, disk_size):
        direction = self.direction_var.get()  # Get the direction (left or right)

        if not direction:
            messagebox.showerror("Input Error", "Direction is required for SCAN algorithm.")
            return

        # Call the SCAN algorithm with the direction
        sequence, total_head_movement = scan(requests, head_position, direction, disk_size)

        # Display results
        result_text = f"Algorithm: SCAN (Elevator)\n"
        result_text += f"Request Sequence: {sequence}\n"
        result_text += f"Total Head Movement: {total_head_movement} cylinders\n"

        self.output_text.config(state="normal")
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, result_text)
        self.output_text.config(state="disabled")

        # Plot timing chart
        plot_disk_head_movement(sequence, "SCAN Disk Scheduling")


    def run_cscan(self, requests, head_position, disk_size):
        direction = self.direction_var.get()  # Get the direction (right or left)
        if not direction:
            messagebox.showerror("Input Error", "Direction is required for C-SCAN algorithm.")
            return

        sequence, total_head_movement = cscan(requests, head_position, disk_size, direction)

        # Display results
        result_text = f"Algorithm: C-SCAN (Circular SCAN)\n"
        result_text += f"Request Sequence: {sequence}\n"
        result_text += f"Total Head Movement: {total_head_movement} cylinders\n"

        self.output_text.config(state="normal")
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, result_text)
        self.output_text.config(state="disabled")

        # Plot timing chart
        plot_disk_head_movement(sequence, "C-SCAN Disk Scheduling")

    def run_look(self, requests, head_position, disk_size):
        direction = self.direction_var.get()
        sequence, total_head_movement = look(requests, head_position, direction)
        
        # Display results
        result_text = f"Algorithm: LOOK\n"
        result_text += f"Request Sequence: {sequence}\n"
        result_text += f"Total Head Movement: {total_head_movement} cylinders\n"
        
        self.output_text.config(state="normal")
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, result_text)
        self.output_text.config(state="disabled")
        
        # Plot timing chart
        plot_disk_head_movement(sequence, "LOOK Disk Scheduling")

    def run_clook(self, requests, head_position):
        sequence, total_head_movement = clook(requests, head_position)
        
        # Display results
        result_text = f"Algorithm: C-LOOK (Circular LOOK)\n"
        result_text += f"Request Sequence: {sequence}\n"
        result_text += f"Total Head Movement: {total_head_movement} cylinders\n"
        
        self.output_text.config(state="normal")
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, result_text)
        self.output_text.config(state="disabled")
        
        # Plot timing chart
        plot_disk_head_movement(sequence, "C-LOOK Disk Scheduling")

    def run_wstsf(self, requests, head_position, disk_size):
        try:
            weights = list(map(int, self.weights_entry.get().split(',')))  # Get the weights from input field
        except ValueError:
            messagebox.showerror("Input Error", "Weights must be a comma-separated list of integers.")
            return

        if len(weights) != len(requests):
            messagebox.showerror("Input Error", "The number of weights must match the number of requests.")
            return

        sequence, total_head_movement = wstsf(requests, head_position, weights, disk_size)

        # Display results
        result_text = f"Algorithm: WSTSF (Weighted Shortest Seek Time First)\n"
        result_text += f"Request Sequence: {sequence}\n"
        result_text += f"Total Head Movement: {total_head_movement} cylinders\n"

        self.output_text.config(state="normal")
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, result_text)
        self.output_text.config(state="disabled")

        # Plot timing chart
        plot_disk_head_movement(sequence, "WSTSF Disk Scheduling")

    def run_priority(self, requests):
        try:
            priorities = list(map(int, self.priorities_entry.get().split(',')))  # Get priorities from input
        except ValueError:
            messagebox.showerror("Input Error", "Priorities must be a comma-separated list of integers.")
            return

        if len(priorities) != len(requests):
            messagebox.showerror("Input Error", "The number of priorities must match the number of requests.")
            return

        sequence = priority_scheduling(requests, priorities)

        # Display results
        result_text = f"Algorithm: Priority Scheduling\n"
        result_text += f"Request Sequence: {sequence}\n"

        self.output_text.config(state="normal")
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, result_text)
        self.output_text.config(state="disabled")

        # Plot timing chart
        plot_disk_head_movement(sequence, "Priority Scheduling Disk Scheduling")


# Main program
if __name__ == "__main__":
    root = tk.Tk()
    app = DiskSchedulingApp(root)
    root.mainloop()
