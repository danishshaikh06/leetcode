import heapq

def prim(graph, start):
    visited = set()
    min_heap = [(0, start)]   # (weight, node)
    
    total_cost = 0

    while min_heap:
        wt, node = heapq.heappop(min_heap)

        if node in visited:
            continue

        visited.add(node)
        total_cost += wt

        for nei, edge_wt in graph[node]:
            if nei not in visited:
                heapq.heappush(min_heap, (edge_wt, nei))

    return total_cost