# Module 2: Simulation Environment (Python)
# This module simulates a mobile/embedded system with varying workloads and tracks energy consumption.



import simpy
import random

# Simulation parameters
NUM_TASKS = 10
TIME_QUANTUM = 3
SIMULATION_TIME = 100

# Task generator
def task_generator(env, scheduler):
    for i in range(NUM_TASKS):
        burst_time = random.randint(1, 15)
        energy_usage = random.randint(1, 3)
        task = {"id": i, "burst_time": burst_time, "energy_usage": energy_usage}
        print(f"Task {i} created with burst time {burst_time} and energy usage {energy_usage}")
        scheduler.add_task(task)
        yield env.timeout(random.randint(1, 5))

# Energy-Efficient Scheduler
class EEScheduler:
    def __init__(self, env):
        self.env = env
        self.tasks = []
        self.total_energy = 0

    def add_task(self, task):
        self.tasks.append(task)

    def run(self):
        while self.tasks:
            task = self.tasks.pop(0)
            print(f"Executing Task {task['id']} at time {self.env.now}")
            remaining_time = task["burst_time"]
            while remaining_time > 0:
                execution_time = min(TIME_QUANTUM, remaining_time)
                self.total_energy += execution_time * task["energy_usage"]
                yield self.env.timeout(execution_time)
                remaining_time -= execution_time
            print(f"Task {task['id']} completed at time {self.env.now}")
        print(f"Total energy consumed: {self.total_energy} units")

# Simulation setup
env = simpy.Environment()
scheduler = EEScheduler(env)
env.process(task_generator(env, scheduler))
env.process(scheduler.run())
env.run(until=SIMULATION_TIME)