# Module 2: Simulation Environment (Python)
# This module simulates a mobile/embedded system with varying workloads and tracks energy consumption.


# simulation.py
from scheduler import Process, CPU, round_robin_scheduling

def calculate_metrics(completed_processes, cpu):
    """
    Calculates performance and energy metrics.
    """
    total_turnaround_time = 0
    total_waiting_time = 0

    for process in completed_processes:
        turnaround_time = process.finish_time - process.arrival_time
        waiting_time = turnaround_time - process.burst_time
        total_turnaround_time += turnaround_time
        total_waiting_time += waiting_time

    avg_turnaround_time = total_turnaround_time / len(completed_processes)
    avg_waiting_time = total_waiting_time / len(completed_processes)

    return {
        "avg_turnaround_time": avg_turnaround_time,
        "avg_waiting_time": avg_waiting_time,
        "total_power_consumption": cpu.power_consumption,
        "idle_time": cpu.idle_time,
    }


def simulate_round_robin(processes, time_quantum):
    """
    Simulates Round Robin scheduling and prints the results.
    """
    print("Simulating Energy-Efficient Round Robin Scheduling...")
    cpu = CPU(base_power=100, max_frequency=3.0, min_frequency=1.0)
    completed_processes = round_robin_scheduling(processes, time_quantum, cpu)

    # Print process execution details
    print("\nProcess Execution Details:")
    for process in completed_processes:
        print(
            f"Process {process.pid}: "
            f"Start Time={process.start_time}, "
            f"Finish Time={process.finish_time}, "
            f"Turnaround Time={process.finish_time - process.arrival_time}, "
            f"Waiting Time={process.finish_time - process.arrival_time - process.burst_time}"
        )

    # Calculate and print performance metrics
    metrics = calculate_metrics(completed_processes, cpu)
    print("\nPerformance Metrics:")
    print(f"Average Turnaround Time: {metrics['avg_turnaround_time']:.2f}")
    print(f"Average Waiting Time: {metrics['avg_waiting_time']:.2f}")
    print(f"Total Power Consumption: {metrics['total_power_consumption']:.2f} Joules")
    print(f"CPU Idle Time: {metrics['idle_time']} units")

    return completed_processes, cpu