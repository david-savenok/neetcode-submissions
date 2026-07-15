class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            to_compare = heapq.nsmallest(2, stones)
            if to_compare[0] == to_compare[1]:
                heapq.heappop(stones)
                heapq.heappop(stones)
            elif to_compare[0] < to_compare[1]:
                temp = to_compare[0] - to_compare[1]
                heapq.heappop(stones)
                heapq.heappop(stones)
                heapq.heappush(stones, temp)
        if len(stones) > 0:
            return -stones[0]
        else:
            return 0
