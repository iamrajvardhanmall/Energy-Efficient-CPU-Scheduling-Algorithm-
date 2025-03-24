import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from scheduler import Process, CPU, round_robin_scheduling

# Function to run the simulation and display results
def run_simulation():
    try:
        # Get process details from the table
        processes = []
        for row in process_table.get_children():
            values = process_table.item(row)["values"]
            pid, arrival_time, burst_time, priority = map(int, values)
            processes.append(Process(pid, arrival_time, burst_time, priority))

        # Get the time quantum
        time_quantum = int(entry_time_quantum.get())

        # Run the simulation
        cpu = CPU(base_power=100, max_frequency=3.0, min_frequency=1.0)
        completed_processes = round_robin_scheduling(processes, time_quantum, cpu)

        # Display process execution details in the result table
        for row in result_table.get_children():
            result_table.delete(row)
        for process in completed_processes:
            turnaround_time = process.finish_time - process.arrival_time
            waiting_time = turnaround_time - process.burst_time
            result_table.insert("", "end", values=(
                process.pid, process.start_time, process.finish_time,
                turnaround_time, waiting_time
            ))

        # Display performance metrics
        total_turnaround_time = sum(p.finish_time - p.arrival_time for p in completed_processes)
        total_waiting_time = sum((p.finish_time - p.arrival_time - p.burst_time) for p in completed_processes)
        avg_turnaround_time = total_turnaround_time / len(completed_processes)
        avg_waiting_time = total_waiting_time / len(completed_processes)

        label_avg_turnaround.config(text=f"Average Turnaround Time: {avg_turnaround_time:.2f}")
        label_avg_waiting.config(text=f"Average Waiting Time: {avg_waiting_time:.2f}")
        label_power_consumption.config(text=f"Total Power Consumption: {cpu.power_consumption:.2f} Joules")
        label_idle_time.config(text=f"CPU Idle Time: {cpu.idle_time} units")

        # Visualize power consumption and Gantt chart
        visualize_power_consumption(completed_processes, cpu)
        visualize_gantt_chart(completed_processes)

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to visualize power consumption
def visualize_power_consumption(completed_processes, cpu):
    time_points = np.arange(0, max(p.finish_time for p in completed_processes) + 1)
    power_consumption = [cpu.base_power * (cpu.current_frequency / cpu.max_frequency) for _ in time_points]

    fig, ax = plt.subplots()
    ax.plot(time_points, power_consumption, label="Power Consumption")
    ax.set_xlabel("Time")
    ax.set_ylabel("Power (Watts)")
    ax.set_title("CPU Power Consumption Over Time")
    ax.legend()

    # Embed the plot in the GUI
    for widget in frame_graph.winfo_children():
        widget.destroy()
    canvas = FigureCanvasTkAgg(fig, master=frame_graph)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Function to visualize Gantt chart
def visualize_gantt_chart(completed_processes):
    fig, ax = plt.subplots()
    start_times = [p.start_time for p in completed_processes]
    burst_times = [p.burst_time for p in completed_processes]
    pids = [p.pid for p in completed_processes]

    ax.barh(pids, burst_times, left=start_times, color='skyblue', edgecolor='black')
    ax.set_xlabel("Time")
    ax.set_ylabel("Processes")
    ax.set_title("Gantt Chart")
    ax.invert_yaxis()

    # Embed the Gantt chart in the GUI
    for widget in frame_gantt.winfo_children():
        widget.destroy()
    canvas = FigureCanvasTkAgg(fig, master=frame_gantt)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Create the main window
root = tk.Tk()
root.title("Energy-Efficient CPU Scheduling")

# Frame for process input
frame_input = ttk.LabelFrame(root, text="Process Input")
frame_input.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

# Table for process details
columns = ("PID", "Arrival Time", "Burst Time", "Priority")
process_table = ttk.Treeview(frame_input, columns=columns, show="headings")
for col in columns:
    process_table.heading(col, text=col)
process_table.grid(row=0, column=0, padx=10, pady=10)

# Frame for time quantum input
frame_quantum = ttk.LabelFrame(root, text="Time Quantum")
frame_quantum.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

label_time_quantum = ttk.Label(frame_quantum, text="Time Quantum:")
label_time_quantum.grid(row=0, column=0, padx=10, pady=10)
entry_time_quantum = ttk.Entry(frame_quantum)
entry_time_quantum.insert(0, "3")
entry_time_quantum.grid(row=0, column=1, padx=10, pady=10)

# Button to run the simulation
button_run = ttk.Button(root, text="Run Simulation", command=run_simulation)
button_run.grid(row=2, column=0, padx=10, pady=10)

# Frame for results
frame_results = ttk.LabelFrame(root, text="Results")
frame_results.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

# Frame for power consumption graph
frame_graph = ttk.LabelFrame(root, text="Power Consumption Graph")
frame_graph.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

# Frame for Gantt chart
frame_gantt = ttk.LabelFrame(root, text="Gantt Chart")
frame_gantt.grid(row=5, column=0, padx=10, pady=10, sticky="ew")

# Start the main loop
root.mainloop()