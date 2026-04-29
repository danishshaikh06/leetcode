def bfs(self, start):
    from collections import deque

    visited = [False] * self.n
    q = deque()
    result = []

    visited[start] = True
    q.append(start)

    while q:
        node = q.popleft()
        result.append(node)

        for neighbor in self.adj[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append(neighbor)

    return result