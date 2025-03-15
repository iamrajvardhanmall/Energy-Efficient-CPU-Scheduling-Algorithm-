import random
from simpy import Environment

# Task generator
def task_generator(env, scheduler):
    task_id = 1
    while True:
        burst_time = random.randint(1, 10)  # Random burst time
        priority = random.randint(1, 5)    # Random priority
        energy_cost = random.randint(1, 5) # Random energy cost
        task = {'id': task_id, 'burst_time': burst_time, 'priority': priority, 'energy_cost': energy_cost}
        print(f"Generated Task {task_id} with burst time {burst_time}, priority {priority}, and energy cost {energy_cost}.")
        scheduler(task)
        task_id += 1
        yield env.timeout(random.randint(1, 3))  # Wait before generating the next task

# Scheduler simulation
def scheduler(task):
    print(f"Scheduling Task {task['id']}...")
    # Simulate task execution
    yield env.timeout(task['burst_time'])
    print(f"Completed Task {task['id']}.")

# Simulation setup
env = Environment()
env.process(task_generator(env, scheduler))
env.run(until=20)  # Run simulation for 20 time units