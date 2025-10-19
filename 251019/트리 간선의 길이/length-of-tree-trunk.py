import sys
from collections import deque

# It's good practice to use sys.stdin.readline for faster I/O.
def solve():
    n = int(input())

    # If there's only one node, the diameter is 0.
    if n == 1:
        print(0)
        return

    # Create an adjacency list to represent the tree.
    # graph[node] will be a list of tuples: (neighbor, weight).
    # We use size n + 1 for 1-based indexing of nodes.
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        parent, child, weight = map(int, input().split())
        # The tree is an undirected graph, so add the edge in both directions.
        graph[parent].append((child, weight))
        graph[child].append((parent, weight))

    def bfs(start_node):
        # Initialize distances array. -1 indicates an unvisited node.
        distances = [-1] * (n + 1)
        queue = deque()

        # Start the BFS from the start_node with a distance of 0.
        distances[start_node] = 0
        queue.append((start_node, 0))
        
        # Variables to track the farthest node found so far
        max_distance = 0
        farthest_node = start_node

        while queue:
            current_node, current_dist = queue.popleft()

            # Check if this node is farther than the farthest found so far
            if current_dist > max_distance:
                max_distance = current_dist
                farthest_node = current_node

            # Explore all neighbors of the current node
            for neighbor, weight in graph[current_node]:
                # If the neighbor has not been visited yet
                if distances[neighbor] == -1:
                    new_dist = current_dist + weight
                    distances[neighbor] = new_dist
                    queue.append((neighbor, new_dist))
        
        return farthest_node, max_distance

    # Step 1: Run BFS from an arbitrary node (e.g., node 1) to find one endpoint of the diameter.
    endpoint, _ = bfs(1)

    # Step 2: Run BFS from that endpoint to find the actual diameter of the tree.
    _, diameter = bfs(endpoint)

    # Print the final result
    print(diameter)

# Execute the solution
solve()