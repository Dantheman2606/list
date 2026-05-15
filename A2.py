# A* Algorithm Example (Shortest Path in a Graph)
# -----------------------------------------------
# This program finds the shortest path using A* search.
# At every step, it displays:
# g(n) = actual cost from start node
# h(n) = heuristic value to goal
# f(n) = g(n) + h(n)

from queue import PriorityQueue

# Graph representation
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 6)],
    'C': [('F', 5)],
    'D': [('G', 4)],
    'E': [('G', 2)],
    'F': [('G', 1)],
    'G': []
}

# Heuristic values (estimated distance to goal G)
heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 4,
    'E': 2,
    'F': 1,
    'G': 0
}

def astar(start, goal):

    # Priority Queue stores (f(n), node)
    open_set = PriorityQueue()
    open_set.put((0, start))

    # Store cost from start to node
    g_cost = {node: float('inf') for node in graph}
    g_cost[start] = 0

    # Store parent nodes for path reconstruction
    parent = {}
    parent[start] = None

    visited = set()

    print("\n===== A* Algorithm Execution =====\n")

    while not open_set.empty():

        current_f, current = open_set.get()

        if current in visited:
            continue

        visited.add(current)

        print(f"\nCurrent Node: {current}")
        print(f"g({current}) = {g_cost[current]}")
        print(f"h({current}) = {heuristic[current]}")
        print(f"f({current}) = {g_cost[current] + heuristic[current]}")

        # Goal reached
        if current == goal:
            print("\nGoal Reached!\n")
            break

        # Explore neighbors
        for neighbor, cost in graph[current]:

            tentative_g = g_cost[current] + cost

            print(f"\nChecking neighbor: {neighbor}")
            print(f"Edge Cost = {cost}")
            print(f"New g({neighbor}) = g({current}) + {cost}")
            print(f"                 = {g_cost[current]} + {cost}")
            print(f"                 = {tentative_g}")

            # If shorter path found
            if tentative_g < g_cost[neighbor]:

                g_cost[neighbor] = tentative_g

                f_value = tentative_g + heuristic[neighbor]

                parent[neighbor] = current

                open_set.put((f_value, neighbor))

                print(f"h({neighbor}) = {heuristic[neighbor]}")
                print(f"f({neighbor}) = {tentative_g} + {heuristic[neighbor]}")
                print(f"              = {f_value}")

    # Reconstruct path
    path = []
    node = goal

    while node is not None:
        path.append(node)
        node = parent[node]

    path.reverse()

    print("Shortest Path:", " -> ".join(path))
    print("Total Cost:", g_cost[goal])


# Driver Code
start_node = 'A'
goal_node = 'G'

astar(start_node, goal_node)