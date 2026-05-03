def has_cycle_dfs(V, adj):
    visited = [False] * V
    rec_stack = [False] * V

    def dfs(node):
        visited[node] = True
        rec_stack[node] = True

        for neighbor in adj[node]:
            if not visited[neighbor]:
                if dfs(neighbor):
                    return True
            elif rec_stack[neighbor]:
                return True  # cycle found

        rec_stack[node] = False
        return False

    for i in range(V):
        if not visited[i]:
            if dfs(i):
                return True

    return False