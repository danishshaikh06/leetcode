class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        from collections import defaultdict

        graph = defaultdict(list)

        # build undirected graph
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        dt = [-1] * n
        low = [-1] * n

        self.time = 0
        bridges = []

        def dfs(node,par):

            dt[node] = low[node] = self.time
            self.time+=1

            for nei in graph[node]:

                if nei == par:
                    continue

                if dt[nei] == -1:
                   dfs(nei,node)

                   low[node] = min(low[node], low[nei])

                   if low[nei] > dt[node]:
                    bridges.append([node,nei])

                else:
                    low[node] = min(low[node], dt[nei])

        for i in range(n):
            if dt[i] == -1:
                dfs(i, -1)

        return bridges


            