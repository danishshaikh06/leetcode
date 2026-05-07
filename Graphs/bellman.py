# bellman ford 

def bellman(edges, n, start):
    dist = [float('inf')] * n
    dist[start] = 0

    for _ in range(n - 1):
        for u, v, wt in edges:
            if dist[u] != float('inf') and dist[v] > dist[u] + wt:
                dist[v] = dist[u] + wt

    return dist

# for negative cycle detection
'''for u, v, wt in edges:
  if dist[u] != float('inf') and dist[v] > dist[u] + wt:
      print("Negative cycle detected")
      return None'''

    

edges = [
    (0, 1, 4), # (u,v,wt)
    (0, 2, 5),
    (1, 2, -3),
    (1, 3, 6),
    (2, 3, 2),
    (3, 4, 1)
]

print(bellman(edges, 5, 0))

