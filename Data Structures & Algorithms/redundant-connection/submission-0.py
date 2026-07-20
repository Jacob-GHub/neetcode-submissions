class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj_list = collections.defaultdict(set)

        for node,neighbor in edges:
            adj_list[node].add(neighbor)
            adj_list[neighbor].add(node)

        def has_cycle(new_adj_list, visited, node, parent):
            visited.add(node)

            for neighbor in new_adj_list[node]:
                if neighbor not in visited:
                    if has_cycle(new_adj_list,visited, neighbor, node): return True
                elif neighbor != parent: return True
            
            return False
            


        for i in range(n-1,-1,-1):
            node, neighbor = edges[i]
            adj_list[node].remove(neighbor)
            adj_list[neighbor].remove(node)
            # print(edges[i], adj_list)
            if not has_cycle(adj_list,set(),edges[0][0],edges[0][1]): 
                return edges[i]

            adj_list[node].add(neighbor)
            adj_list[neighbor].add(node)
        
        return []



