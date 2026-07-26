class Solution:
    def rob(self, nums: List[int]) -> int:
        HR = [[0] * (len(nums) + 1) for _ in range(len(nums) + 1)]

        for i in range(len(nums) - 1, -1, -1):
            for j in range(-1, i + 1):
                if j == i - 1:
                    HR[i][j] = HR[i + 1][j]
                else:
                    HR[i][j] = max(nums[i] + HR[i + 1][i], HR[i + 1][j])
        for i in HR:
            print(i)
        return max(HR[0][0], HR[0][-1])