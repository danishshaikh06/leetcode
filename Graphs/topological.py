from collections import defaultdict

def topological_sort_dfs(V, edges):
    graph = defaultdict(list)
    
    # Build graph
    for u, v in edges:
        graph[u].append(v)
    
    visited = [False] * V
    stack = []

    def dfs(node):
        visited[node] = True
        
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)
        
        stack.append(node)

    # Call DFS for all nodes
    for i in range(V):
        if not visited[i]:
            dfs(i)

    # Reverse stack to get order
    return stack[::-1]


# Example
V = 6
edges = [(5,2), (5,0), (4,0), (4,1), (2,3), (3,1)]

print(topological_sort_dfs(V, edges))