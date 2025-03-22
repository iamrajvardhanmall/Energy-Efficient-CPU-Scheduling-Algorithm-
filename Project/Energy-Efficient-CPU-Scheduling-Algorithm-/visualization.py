# Module 3: Performance Analysis and Visualization (Python)
# This module analyzes and visualizes the results of the simulation.



# visualization.py
import matplotlib.pyplot as plt
import numpy as np

def visualize_power_consumption(completed_processes, cpu):
    """
    Visualizes power consumption over time.
    """
    time_points = np.arange(0, max(p.finish_time for p in completed_processes) + 1)
    power_consumption = [cpu.base_power * (cpu.current_frequency / cpu.max_frequency) for _ in time_points]

    plt.plot(time_points, power_consumption, label="Power Consumption")
    plt.xlabel("Time")
    plt.ylabel("Power (Watts)")
    plt.title("CPU Power Consumption Over Time")
    plt.legend()
    plt.show()