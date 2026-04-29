def dfs_util(self, node, visited, result):
    visited[node] = True
    result.append(node)

    for neighbor in self.adj[node]:
        if not visited[neighbor]:
            self.dfs_util(neighbor, visited, result)

def dfs(self, start):
    visited = [False] * self.n
    result = []
    self.dfs_util(start, visited, result)
    return result