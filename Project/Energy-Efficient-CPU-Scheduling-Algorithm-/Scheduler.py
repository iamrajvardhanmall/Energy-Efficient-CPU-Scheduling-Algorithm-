# The code is divided into three modules: Algorithm Design, Simulation Environment, and Performance Analysis. 
# The implementation uses C++ for the scheduling algorithm and Python for simulation and visualization.



# Module 1: Algorithm Design and Implementation (C++)
# This module implements the Energy-Efficient Round Robin (EE-RR) algorithm with Dynamic Frequency Scaling (DVFS) and Idle State Optimization.


# scheduler.py
class Process:
    def __init__(self, pid, arrival_time, burst_time, priority):
        self.pid = pid  # Process ID
        self.arrival_time = arrival_time  # Arrival time
        self.burst_time = burst_time  # Total CPU time required
        self.remaining_time = burst_time  # Remaining CPU time
        self.priority = priority  # Priority (lower value = higher priority)
        self.start_time = None  # Time when the process starts execution
        self.finish_time = None  # Time when the process finishes execution

    def __str__(self):
        return f"Process {self.pid}: Arrival={self.arrival_time}, Burst={self.burst_time}, Priority={self.priority}"


class CPU:
    def __init__(self, base_power, max_frequency, min_frequency):
        self.base_power = base_power  # Base power consumption (Watts)
        self.max_frequency = max_frequency  # Maximum CPU frequency (GHz)
        self.min_frequency = min_frequency  # Minimum CPU frequency (GHz)
        self.current_frequency = max_frequency  # Current CPU frequency
        self.power_consumption = 0  # Total power consumed (Joules)
        self.idle_time = 0  # Total time CPU is idle

    def execute(self, process, time_quantum):
        """
        Execute a process for a given time quantum and update power consumption.
        """
        execution_time = min(time_quantum, process.remaining_time)
        process.remaining_time -= execution_time

        # Adjust frequency based on priority (DVFS)
        if process.priority > 1:  # Lower priority tasks use lower frequency
            self.current_frequency = self.min_frequency
        else:
            self.current_frequency = self.max_frequency

        # Calculate power consumption (simplified model: Power = Base Power * Frequency)
        power = self.base_power * (self.current_frequency / self.max_frequency)
        self.power_consumption += power * execution_time

        return execution_time

    def idle(self, time):
        """
        Simulate CPU idle state (low power mode).
        """
        self.idle_time += time
        self.power_consumption += 0.1 * time  # Low power consumption during idle


def round_robin_scheduling(processes, time_quantum, cpu):
    """
    Simulates Round Robin scheduling with energy efficiency features.
    """
    current_time = 0
    ready_queue = []  # Queue to hold processes ready for execution
    completed_processes = []  # List to store completed processes

    while processes or ready_queue:
        # Add processes to the ready queue if they have arrived
        while processes and processes[0].arrival_time <= current_time:
            ready_queue.append(processes.pop(0))

        if not ready_queue:
            # No processes are ready; CPU is idle
            cpu.idle(1)
            current_time += 1
            continue

        # Get the next process from the ready queue
        current_process = ready_queue.pop(0)

        # Record start time if not already set
        if current_process.start_time is None:
            current_process.start_time = current_time

        # Execute the process
        execution_time = cpu.execute(current_process, time_quantum)
        current_time += execution_time

        # Check if the process has completed
        if current_process.remaining_time == 0:
            current_process.finish_time = current_time
            completed_processes.append(current_process)
        else:
            # Re-add the process to the ready queue if it hasn't completed
            ready_queue.append(current_process)

    return completed_processes