#include <iostream>
#include <algorithm>
using namespace std;

struct Job {
    char id;
    int deadline;
    int profit;
};

// Sort jobs by profit (descending)
bool compare(Job a, Job b) {
    return a.profit > b.profit;
}

int main() {

    Job jobs[] = {
        {'A', 2, 100},
        {'B', 1, 19},
        {'C', 2, 27},
        {'D', 1, 25},
        {'E', 3, 15}
    };

    int n = 5;

    // Sort jobs according to profit
    sort(jobs, jobs + n, compare);

    int result[3];
    bool slot[3] = {false};

    // Initialize result array
    for(int i = 0; i < 3; i++)
        result[i] = -1;

    // Perform scheduling
    for(int i = 0; i < n; i++) {

        // Find free slot
        for(int j = min(3, jobs[i].deadline) - 1; j >= 0; j--) {

            if(slot[j] == false) {
                result[j] = i;
                slot[j] = true;
                break;
            }
        }
    }

    cout << "Selected Jobs:\n";

    for(int i = 0; i < 3; i++) {
        if(result[i] != -1)
            cout << jobs[result[i]].id << " ";
    }

    return 0;
}