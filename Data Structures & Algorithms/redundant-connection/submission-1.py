class Solution:
    def findRedundantConnection(self, edges):
        n = len(edges)

        parent = list(range(n + 1))
        size = [1] * (n + 1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)

            if rootX == rootY:
                return False

            if size[rootX] >= size[rootY]:
                parent[rootY] = rootX
                size[rootX] += size[rootY]
            else:
                parent[rootX] = rootY
                size[rootY] += size[rootX]

            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]