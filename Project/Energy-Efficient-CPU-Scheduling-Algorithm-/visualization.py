import matplotlib.pyplot as plt

# Example data (replace with actual simulation results)
tasks = [1, 2, 3, 4, 5]
energy_consumed = [15, 10, 20, 12, 18]  # Energy consumed per task
completion_time = [5, 3, 7, 4, 6]      # Completion time per task

# Plot energy consumption
plt.figure(figsize=(10, 5))
plt.bar(tasks, energy_consumed, color='blue')
plt.title("Energy Consumption per Task")
plt.xlabel("Task ID")
plt.ylabel("Energy Consumed (units)")
plt.show()

# Plot completion time
plt.figure(figsize=(10, 5))
plt.bar(tasks, completion_time, color='yellow')
plt.title("Task Completion Time")
plt.xlabel("Task ID")
plt.ylabel("Completion Time (units)")
plt.show()

# Compare with traditional scheduling (example)
traditional_energy = [20, 15, 25, 18, 22]  # Example data
plt.figure(figsize=(10, 5))
plt.bar(tasks, energy_consumed, color='blue', label='Energy-Efficient Scheduler')
plt.bar(tasks, traditional_energy, color='red', alpha=0.5, label='Traditional Scheduler')
plt.title("Energy Consumption Comparison")
plt.xlabel("Task ID")         
plt.ylabel("Energy Consumed (units)")
plt.legend()
plt.show()