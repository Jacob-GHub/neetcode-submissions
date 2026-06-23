class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        visited = set()
        adjList = collections.defaultdict(list)
        for edge1, edge2 in edges:
            adjList[edge1].append(edge2)
            adjList[edge2].append(edge1)
        res = 0
        def dfs(edge,parent):
            if edge in visited:
                return 
            visited.add(edge)
            for neighbor in adjList[edge]:
                if neighbor != parent:
                    dfs(neighbor,edge)
            return
        for edge in range(n):
            if edge not in visited:
                res+=1
                dfs(edge,-1)
        return res
        