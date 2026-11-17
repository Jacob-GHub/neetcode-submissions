class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.min_heap = []
        self.k = k
        
        for num in nums:
            if len(self.min_heap) < k:
                heapq.heappush(self.min_heap, num)
            elif len(self.min_heap) == k and num > self.min_heap[0]:
                heapq.heappop(self.min_heap)
                heapq.heappush(self.min_heap, num)

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
            return self.min_heap[0]

        elif self.min_heap and val > self.min_heap[0]:
            heapq.heappop(self.min_heap)
            heapq.heappush(self.min_heap, val)
        return self.min_heap[0]
        
