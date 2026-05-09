# krushals algo -> To find MST but without any cycle 

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])   # path compression
        return self.parent[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)

        if px == py:
            return False   # cycle

        # union by rank
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1

        return True

def kruskal(n, edges):

    edges.sort(key=lambda x: x[2])   # sort by weight

    dsu = DSU(n)

    mst_cost = 0
    mst_edges = []

    for u, v, wt in edges:

        # add edge only if no cycle forms
        if dsu.union(u, v):
            mst_cost += wt
            mst_edges.append((u, v, wt))

    return mst_cost, mst_edges

edges = [
    (0,1,4),
    (0,2,3),
    (1,2,1),
    (1,3,2),
    (2,3,5)
]

n = 4

cost, mst = kruskal(n, edges)

print(cost)
print(mst)