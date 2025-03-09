import heapq
import time

# Define power states (frequency in GHz, voltage in V, and power consumption in W)
POWER_STATES = {
    "high_performance": {"frequency": 2.5, "voltage": 1.2, "power": 5.0},
    "balanced": {"frequency": 1.5, "voltage": 1.0, "power": 3.0},
    "power_saving": {"frequency": 0.8, "voltage": 0.8, "power": 1.5},
}

# Task class to represent tasks
class Task:
    def __init__(self, id, priority, burst_time):
        self.id = id
        self.priority = priority  # Lower value means higher priority
        self.burst_time = burst_time  # Time required to complete the task

    def __lt__(self, other):
        return self.priority < other.priority  # For priority queue

# DVFS Scheduler class
class DVFSScheduler:
    def __init__(self):
        self.current_state = "balanced"  # Start with balanced power state
        self.tasks = []  # Priority queue for tasks
        self.total_energy = 0  # Total energy consumed
        self.total_time = 0  # Total time elapsed

    def add_task(self, task):
        heapq.heappush(self.tasks, task)  # Add task to the priority queue

    def execute_tasks(self):
        while self.tasks:
            task = heapq.heappop(self.tasks)  # Get the highest priority task
            print(f"Executing Task {task.id} (Priority: {task.priority}, Burst Time: {task.burst_time})")

            # Adjust power state based on task priority
            if task.priority < 2:  # High-priority task
                self.set_power_state("high_performance")
            elif task.priority < 5:  # Medium-priority task
                self.set_power_state("balanced")
            else:  # Low-priority task
                self.set_power_state("power_saving")

            # Simulate task execution
            execution_time = task.burst_time / POWER_STATES[self.current_state]["frequency"]
            energy_consumed = POWER_STATES[self.current_state]["power"] * execution_time

            self.total_time += execution_time
            self.total_energy += energy_consumed

            print(f"  Power State: {self.current_state}")
            print(f"  Execution Time: {execution_time:.2f}s")
            print(f"  Energy Consumed: {energy_consumed:.2f}J\n")
            time.sleep(1)  # Simulate time delay

    def set_power_state(self, state):
        self.current_state = state
        print(f"Switching to {state} mode (Frequency: {POWER_STATES[state]['frequency']}GHz, Voltage: {POWER_STATES[state]['voltage']}V)")

    def get_summary(self):
        print("\n--- Simulation Summary ---")
        print(f"Total Time Elapsed: {self.total_time:.2f}s")
        print(f"Total Energy Consumed: {self.total_energy:.2f}J")

# Main function to test the scheduler
if __name__ == "__main__":
    scheduler = DVFSScheduler()

    # Add tasks (ID, Priority, Burst Time)
    scheduler.add_task(Task(1, 1, 10))  # High-priority task
    scheduler.add_task(Task(2, 3, 5))   # Medium-priority task
    scheduler.add_task(Task(3, 6, 8))   # Low-priority task

    # Execute tasks
    scheduler.execute_tasks()

    # Print summary
    scheduler.get_summary()