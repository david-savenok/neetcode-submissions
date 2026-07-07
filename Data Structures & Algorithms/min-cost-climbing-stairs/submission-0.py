class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        MCCS = [0 for i in range(n + 2)]
        for i in range (n - 1, -1, -1):
            MCCS[i] = cost[i] + min(MCCS[i + 1], MCCS[i + 2])
        return min(MCCS[0], MCCS[1])
        