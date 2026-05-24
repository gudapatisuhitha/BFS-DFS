# Graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def bfs(graph, start):
    visited = set()          # To keep track of visited nodes
    queue = deque([start])   # Initialize queue with start node

    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        # Visit all adjacent nodes
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Start BFS traversal from node 'A'
bfs(graph, 'A')
