class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minheap = nums
        heapq.heapify(nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.minheap, val)
        largest = heapq.nlargest(self.k, self.minheap)
        return largest[-1]

