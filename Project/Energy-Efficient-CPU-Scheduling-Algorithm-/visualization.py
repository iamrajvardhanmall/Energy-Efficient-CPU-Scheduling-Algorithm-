# Module 3: Performance Analysis and Visualization (Python)
# This module analyzes and visualizes the results of the simulation.




import matplotlib.pyplot as plt

# Sample data (replace with actual simulation results)
algorithms = ["Round Robin", "Energy-Efficient RR"]
energy_consumption = [120, 80]  # Example energy consumption values
task_completion_times = [50, 45]  # Example task completion times

# Plot energy consumption
plt.figure(figsize=(10, 5))
plt.bar(algorithms, energy_consumption, color=["blue", "green"])
plt.title("Energy Consumption Comparison")
plt.ylabel("Energy Consumed (units)")
plt.show()

# Plot task completion times
plt.figure(figsize=(10, 5))
plt.bar(algorithms, task_completion_times, color=["orange", "red"])
plt.title("Task Completion Time Comparison")
plt.ylabel("Completion Time (units)")
plt.show()