# Dijkstra's Algoritm 
import heapq

def dijkstra(graph, start):
  n = len(graph)
  dist = [float('inf')] * n
  dist[start] = 0

  pq = [(0, start)]

  while pq:
    curr_dist , node = heapq.heappop(pq)

    if curr_dist > dist[node]:
      continue

    # check for neighbor 
    for neig ,wt in graph[node]:
      new_dist = curr_dist + wt

      if dist[neig] > new_dist:
        dist[neig] = new_dist

        heapq.heappush(pq,(new_dist, neig))

  return dist

graph = [
    [(1, 2), (2, 4), (3, 1)],
    [(0, 2), (3, 3)],
    [(0, 4), (3, 5)],
    [(0, 1), (1, 3), (2, 5), (4, 1)],
    [(3, 1)]
]

start = 0 
print(dijkstra(graph, start))
