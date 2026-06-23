class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = collections.defaultdict(list)
        for edg1,edg2 in edges:
            adjList[edg1].append(edg2)
            adjList[edg2].append(edg1)
        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False  # Found a cycle
            visited.add(node)
            
            for neighbor in adjList[node]:
                if neighbor != parent:  # Avoid going back to the parent
                    if not dfs(neighbor, node):
                        return False  # Cycle detected
            return True

        if not dfs(0,-1):
            return False
        return len(visited) == n

        
        