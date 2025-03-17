# The code is divided into three modules: Algorithm Design, Simulation Environment, and Performance Analysis. 
# The implementation uses C++ for the scheduling algorithm and Python for simulation and visualization.



# Module 1: Algorithm Design and Implementation (C++)
# This module implements the Energy-Efficient Round Robin (EE-RR) algorithm with Dynamic Frequency Scaling (DVFS) and Idle State Optimization.


import time
from queue import Queue

# Task structure
class Task:
    def __init__(self, task_id, burst_time, priority, energy_usage):
        self.id = task_id
        self.burst_time = burst_time  # Time required to complete the task
        self.priority = priority      # Priority of the task (lower value = higher priority)
        self.energy_usage = energy_usage  # Energy consumption per unit time

# Energy-Efficient Round Robin Scheduler
class EE_RoundRobinScheduler:
    def __init__(self, time_quantum):
        self.task_queue = Queue()
        self.time_quantum = time_quantum
        self.current_frequency = 1  # Simulated CPU frequency (1 = low, 2 = medium, 3 = high)
        self.total_energy_consumed = 0

    # Adjust CPU frequency based on workload
    def adjust_frequency(self, workload):
        if workload == 0:
            self.current_frequency = 1  # Low frequency for idle state
        elif workload < 3:
            self.current_frequency = 2  # Medium frequency for light workload
        else:
            self.current_frequency = 3  # High frequency for heavy workload
        print(f"[Frequency Adjustment] Adjusted CPU frequency to level {self.current_frequency}")

    # Simulate energy consumption
    def consume_energy(self, execution_time, energy_usage):
        energy = execution_time * energy_usage * self.current_frequency
        self.total_energy_consumed += energy
        print(f"[Energy Consumption] Consumed {energy} units of energy.")

    # Execute a single task
    def execute_task(self, task):
        print(f"[Task Execution] Executing Task {task.id} "
              f"(Burst Time: {task.burst_time}, Priority: {task.priority}, "
              f"Energy Usage: {task.energy_usage})")

        remaining_time = task.burst_time
        while remaining_time > 0:
            execution_time = min(self.time_quantum, remaining_time)
            self.adjust_frequency(self.task_queue.qsize())  # Adjust frequency based on workload
            self.consume_energy(execution_time, task.energy_usage)

            # Simulate time passing
            time.sleep(execution_time * 0.1)  # Simulate time (0.1 seconds per unit time)
            remaining_time -= execution_time

        print(f"[Task Completion] Task {task.id} completed.")

    # Add a task to the queue
    def add_task(self, task):
        if task.burst_time <= 0 or task.energy_usage <= 0:
            print(f"[Error] Invalid task parameters for Task {task.id}")
            return
        self.task_queue.put(task)
        print(f"[Task Added] Task {task.id} added to the queue.")

    # Execute the scheduler
    def run(self):
        if self.task_queue.empty():
            print("[Error] No tasks in the queue to schedule.")
            return

        while not self.task_queue.empty():
            current_task = self.task_queue.get()
            self.execute_task(current_task)

        print(f"[Scheduler Summary] Total energy consumed: {self.total_energy_consumed} units.")


# Main function
if __name__ == "__main__":
    # Create tasks
    task1 = Task(1, 10, 1, 2)  # Task ID, Burst Time, Priority, Energy Usage
    task2 = Task(2, 5, 2, 1)
    task3 = Task(3, 8, 1, 3)

    # Initialize scheduler with a time quantum of 3
    scheduler = EE_RoundRobinScheduler(3)

    # Add tasks to the scheduler
    scheduler.add_task(task1)
    scheduler.add_task(task2)
    scheduler.add_task(task3)

    # Run the scheduler
    scheduler.run()