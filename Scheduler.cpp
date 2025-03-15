#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

// Task structure
struct Task {
    int id;
    int burst_time; // CPU time required
    int priority;   // Lower value means higher priority
    int energy_cost; // Energy cost per unit time
};

// Comparator for priority queue (lower priority value has higher priority)
struct ComparePriority {
    bool operator()(const Task& t1, const Task& t2) {
        return t1.priority > t2.priority;
    }
};

// Energy-efficient scheduler
void energyEfficientScheduler(vector<Task>& tasks) {
    priority_queue<Task, vector<Task>, ComparePriority> pq;

    // Add all tasks to the priority queue
    for (const auto& task : tasks) {
        pq.push(task);
    }

    int current_time = 0;
    int total_energy = 0;

    while (!pq.empty()) {
        Task current_task = pq.top();
        pq.pop();

        // Simulate dynamic frequency scaling
        int frequency = (current_task.burst_time > 5) ? 2 : 1; // Lower frequency for longer tasks
        int execution_time = current_task.burst_time / frequency;

        // Update energy consumption
        total_energy += current_task.energy_cost * execution_time;

        // Simulate task execution
        cout << "Executing Task " << current_task.id << " at frequency " << frequency
             << " for " << execution_time << " units of time." << endl;

        current_time += execution_time;
    }

    cout << "Total Energy Consumed: " << total_energy << " units." << endl;
}

int main() {
    // Example tasks
    vector<Task> tasks = {
        {1, 10, 2, 3}, // Task ID, Burst Time, Priority, Energy Cost
        {2, 5, 1, 2},
        {3, 8, 3, 4}
    };

    // Run the scheduler
    energyEfficientScheduler(tasks);

    return 0;
}