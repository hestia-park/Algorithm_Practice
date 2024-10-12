def bfs(graph, start):
    visited = []  # List to store visited nodes
    queue = [start]  # Initialize a queue with the starting node

    while queue:
        node = queue.pop(0)  # Dequeue the front item from the queue
        if node not in visited:
            visited.append(node)  # Mark the current node as visited

            # Add unvisited neighbors of the current node to the queue
            neighbors = graph[node]
            for neighbor in neighbors:
                queue.append(neighbor)

    return visited

def bfs_re(graph, start,visited):
    # visited = []  # List to store visited nodes
    queue = [start]  # Initialize a queue with the starting node

    while queue:
        node = queue.pop(0)  # Dequeue the front item from the queue
        if node not in visited:
            visited.append(node)  # Mark the current node as visited

            # Add unvisited neighbors of the current node to the queue
            neighbors = graph[node]
            for neighbor in neighbors:
                queue.append(neighbor)
        bfs_re(graph, queue, visited)

    return visited
# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
start_node = 'A'

result = bfs(graph, start_node)
print("BFS traversal:", result)
visited = []
result = bfs_re(graph, start_node,visited)
print("BFS traversal:", result)
