class Solution:
    def climbStairs(self, n: int) -> int:
        """
        if n == 2:
            return 2
        if n == 1:
            return 1
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
        """

        climbStairsArr = [1, 2]
        for i in range(2, n):
            climbStairsArr.append(climbStairsArr[i - 1] + climbStairsArr[i - 2])
        return climbStairsArr[n - 1]
