class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        Q = deque([(0,0)])
        visited = set()
        adj_list = collections.defaultdict(list)

        for node, neighbor in edges:
            if node == neighbor: return False
            adj_list[node].append(neighbor)
            adj_list[neighbor].append(node)

        while Q:
            n_layer = len(Q)
            for _ in range(n_layer):
                cur_node, parent = Q.popleft()
                visited.add(cur_node)

                for neighbor in adj_list[cur_node]:
                    if neighbor in visited and neighbor != parent:
                        return False
                    if neighbor != parent:
                        Q.append((neighbor,cur_node))
        
        return len(visited) == n

        