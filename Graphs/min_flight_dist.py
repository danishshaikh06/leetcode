class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        import heapq
        from collections import defaultdict
        graph = defaultdict(list)

        # graph for directed
        for u,v,cost in flights:
            graph[u].append((v,cost))

        # perform dijkstra's
        pq =[(0,src,-1)]

        dist = {}
        
        while pq:
            cost, node, stop = heapq.heappop(pq)

            if node == dst:
                return cost 

            if stop >=k:
                continue 
            
            if (node,stop) in dist and dist[(node,stop)] <= cost:
                continue

            dist[(node,stop)] = cost

        # check for neighbor
            for neig, wt in graph[node]:
                new_cost = cost + wt
                heapq.heappush(pq, (new_cost, neig, stop + 1))

        return -1 

   

        