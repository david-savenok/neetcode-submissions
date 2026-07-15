class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minheap = nums
        heapq.heapify(nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.minheap, val)
        return heapq.nlargest(self.k, self.minheap)[-1]       