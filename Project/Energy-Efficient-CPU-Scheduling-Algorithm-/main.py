# This file ties everything together and runs the simulation.

from scheduler import Process
from simulation import simulate_round_robin
from visualization import visualize_power_consumption

if __name__ == "__main__":
    # Define a list of processes (PID, Arrival Time, Burst Time, Priority)
    processes = [
        Process(1, 0, 100, 1),
        Process(2, 1, 5, 2),
        Process(3, 2, 8, 1),
        Process(4, 3, 2, 2),
    ]

    # Set the time quantum
    time_quantum = 3

    # Simulate Round Robin scheduling
    completed_processes, cpu = simulate_round_robin(processes, time_quantum)

    # Visualize power consumption
    visualize_power_consumption(completed_processes, cpu)