class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = collections.defaultdict(list)
        distances = [float('inf') for _ in range(n+1)]
        distances[k] = 0
        distances[0] = -1

        for node, neighbor, time in times:
            adj_list[node].append((neighbor,time))
        
        Q = deque([(k,0)])

        while Q:
            cur_node,run_time = Q.popleft()

            for neighbor,time in adj_list[cur_node]:
                if distances[neighbor] > run_time + time:
                    distances[neighbor] = run_time + time
                    Q.append((neighbor,run_time + time))
        
        ans = max(distances)
        return ans if ans != float('inf') else -1