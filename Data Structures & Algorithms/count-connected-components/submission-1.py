class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        adj_list = collections.defaultdict(list)

        for node, neighbor in edges:
            adj_list[node].append(neighbor)
            adj_list[neighbor].append(node)


        def dfs(node):
            visited.add(node)

            for neighbor in adj_list[node]:
                if neighbor not in visited: 
                    dfs(neighbor)


        connected_comps = 0
        for node in range(n):
            if node not in visited:
                connected_comps += 1
                dfs(node)

        return connected_comps
                