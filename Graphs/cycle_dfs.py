def dfs(node, parent, adj, visited):
    visited[node] = True

    for neighbor in adj[node]:
        if not visited[neighbor]:
            if dfs(neighbor, node, adj, visited):
                return True
        elif neighbor != parent:
            return True  # cycle detected

    return False


def has_cycle(V, adj):
    visited = [False] * V

    for i in range(V):
        if not visited[i]:
            if dfs(i, -1, adj, visited):
                return True

    return False