#include <iostream>
#include <queue>
#include <vector>
#include <unistd.h> // for sleep()

using namespace std;

// Define power states (frequency in GHz, voltage in V, and power consumption in W)
struct PowerState {
    double frequency; // in GHz
    double voltage;   // in V
    double power;     // in W
};

// Define power states
const PowerState POWER_STATES[] = {
    {2.5, 1.2, 5.0}, // high_performance
    {1.5, 1.0, 3.0}, // balanced
    {0.8, 0.8, 1.5}  // power_saving
};

// Task class to represent tasks
class Task {
public:
    int id;
    int priority;    // Lower value means higher priority
    int burst_time;  // Time required to complete the task

    Task(int id, int priority, int burst_time)
        : id(id), priority(priority), burst_time(burst_time) {}

    // Overload < operator for priority queue
    bool operator<(const Task& other) const {
        return priority > other.priority; // Min-heap based on priority
    }
};

// DVFS Scheduler class
class DVFSScheduler {
private:
    string current_state; // Current power state
    priority_queue<Task> tasks; // Priority queue for tasks
    double total_energy; // Total energy consumed
    double total_time;   // Total time elapsed

public:
    DVFSScheduler() : current_state("balanced"), total_energy(0), total_time(0) {}

    void add_task(const Task& task) {
        tasks.push(task); // Add task to the priority queue
    }

    void execute_tasks() {
        while (!tasks.empty()) {
            Task task = tasks.top(); // Get the highest priority task
            tasks.pop();

            cout << "Executing Task " << task.id 
                 << " (Priority: " << task.priority 
                 << ", Burst Time: " << task.burst_time << ")\n";

            // Adjust power state based on task priority
            if (task.priority < 2) { // High-priority task
                set_power_state("high_performance");
            } else if (task.priority < 5) { // Medium-priority task
                set_power_state("balanced");
            } else { // Low-priority task
                set_power_state("power_saving");
            }

            // Simulate task execution
            double execution_time = task.burst_time / POWER_STATES[get_state_index(current_state)].frequency;
            double energy_consumed = POWER_STATES[get_state_index(current_state)].power * execution_time;

            total_time += execution_time;
            total_energy += energy_consumed;

            cout << "  Power State: " << current_state << "\n";
            cout << "  Execution Time: " << execution_time << "s\n";
            cout << "  Energy Consumed: " << energy_consumed << "J\n\n";
            sleep(1); // Simulate time delay
        }
    }

    void set_power_state(const string& state) {
        current_state = state;
        cout << "Switching to " << state << " mode "
             << "(Frequency: " << POWER_STATES[get_state_index(state)].frequency << "GHz, "
             << "Voltage: " << POWER_STATES[get_state_index(state)].voltage << "V)\n";
    }

    void get_summary() const {
        cout << "\n--- Simulation Summary ---\n";
        cout << "Total Time Elapsed: " << total_time << "s\n";
        cout << "Total Energy Consumed: " << total_energy << "J\n";
    }

private:
    // Helper function to get the index of a power state
    int get_state_index(const string& state) const {
        if (state == "high_performance") return 0;
        if (state == "balanced") return 1;
        if (state == "power_saving") return 2;
        return -1; // Invalid state
    }
};

// Main function to test the scheduler
int main() {
    DVFSScheduler scheduler;

    // Add tasks (ID, Priority, Burst Time)
    scheduler.add_task(Task(1, 1, 10)); // High-priority task
    scheduler.add_task(Task(2, 3, 5));  // Medium-priority task
    scheduler.add_task(Task(3, 6, 8));  // Low-priority task

    // Execute tasks
    scheduler.execute_tasks();

    // Print summary
    scheduler.get_summary();

    return 0;
}