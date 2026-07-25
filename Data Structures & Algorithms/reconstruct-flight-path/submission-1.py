class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj_list = collections.defaultdict(list)

        for source,dest in sorted(tickets, reverse = True):
            adj_list[source].append(dest)
        
        path = []
        def dfs(node):
            while adj_list[node]:
                dfs(adj_list[node].pop())
            path.append(node)
        
        dfs("JFK")
        return path[::-1]


