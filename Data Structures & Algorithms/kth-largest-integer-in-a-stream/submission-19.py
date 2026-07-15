class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minheap = []
        heapq.heapify(self.minheap)
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.minheap) > self.k - 1 and self.minheap[0] < val:
            heapq.heappop(self.minheap)
        if len(self.minheap) < self.k:
            heapq.heappush(self.minheap, val)   
        return self.minheap[0]