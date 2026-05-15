#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class Graph {
    int vertices;
    vector<vector<int>> adj;

public:
    // Constructor
    Graph(int v) {
        vertices = v;
        adj.resize(v);
    }

    // Add edge for undirected graph
    void addEdge(int u, int v) {
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    // Recursive DFS function
    void DFSUtil(int v, vector<bool>& visited) {
        visited[v] = true;
        cout << v << " ";

        for (int neighbor : adj[v]) {
            if (!visited[neighbor]) {
                DFSUtil(neighbor, visited);
            }
        }
    }

    // DFS traversal
    void DFS(int start) {
        vector<bool> visited(vertices, false);

        cout << "DFS Traversal: ";
        DFSUtil(start, visited);
        cout << endl;
    }

    // BFS traversal
    void BFS(int start) {
        vector<bool> visited(vertices, false);
        queue<int> q;

        visited[start] = true;
        q.push(start);

        cout << "BFS Traversal: ";

        while (!q.empty()) {
            int current = q.front();
            q.pop();

            cout << current << " ";

            for (int neighbor : adj[current]) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    q.push(neighbor);
                }
            }
        }

        cout << endl;
    }
};

int main() {
    Graph g(6);

    // Adding edges
    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 3);
    g.addEdge(1, 4);
    g.addEdge(2, 5);

    // Perform DFS and BFS
    g.DFS(0);
    g.BFS(0);

    return 0;
}