#include <iostream>
#include <climits>
using namespace std;

#define V 5

int minDistance(int dist[], bool visited[]) {

    int min = INT_MAX, minIndex;

    for(int v = 0; v < V; v++) {
        if(visited[v] == false && dist[v] <= min) {
            min = dist[v];
            minIndex = v;
        }
    }

    return minIndex;
}

void dijkstra(int graph[V][V], int src) {

    int dist[V];
    bool visited[V];

    // Initialize distances
    for(int i = 0; i < V; i++) {
        dist[i] = INT_MAX;
        visited[i] = false;
    }

    dist[src] = 0;

    // Find shortest path
    for(int count = 0; count < V - 1; count++) {

        int u = minDistance(dist, visited);

        visited[u] = true;

        for(int v = 0; v < V; v++) {

            if(!visited[v] &&
               graph[u][v] &&
               dist[u] != INT_MAX &&
               dist[u] + graph[u][v] < dist[v]) {

                dist[v] = dist[u] + graph[u][v];
            }
        }
    }

    cout << "Vertex \t Distance from Source\n";

    for(int i = 0; i < V; i++)
        cout << i << "\t\t" << dist[i] << endl;
}

int main() {

    int graph[V][V] = {
        {0, 10, 0, 5, 0},
        {0, 0, 1, 2, 0},
        {0, 0, 0, 0, 4},
        {0, 3, 9, 0, 2},
        {7, 0, 6, 0, 0}
    };

    dijkstra(graph, 0);

    return 0;
}