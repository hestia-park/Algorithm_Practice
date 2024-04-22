def dfs_stack(graph, start_node):
    # visited = [False] * len(graph)
    stack = [start_node]

    while stack:
        node = stack.pop()
        if not visited[node]:
            print(node, end=" ")  # Process the current node
            visited[node] = True

            for neighbor in graph[node]:
                if not visited[neighbor]:
                    stack.append(neighbor)
def dfs_recursive(graph, node, visited):
    visited[node] = True
    print(node, end=" ")  # Process the current node

    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs_recursive(graph, neighbor, visited)




def dfs(graph,start_p):

    stack=[start_p]
    while stack:
        node=stack.pop()
        if not visited[node]:
            print(node, end=" ")
            visited[node]=True
            for noe in graph[node]:
                if not visited[noe]:
                    stack.append((noe))
# Example usage (same graph as above):
graph = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
}
visited=[False] *len(graph)
start_node = 0
dfs_stack(graph, start_node)
visited=[False] *len(graph)
dfs(graph, start_node)
visited=[False] *len(graph)
start_node = 0
dfs_recursive(graph, start_node, visited)