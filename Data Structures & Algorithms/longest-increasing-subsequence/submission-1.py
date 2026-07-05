class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        nums.append(min(nums) - 1)
        LIS = [[0] * (n + 1) for _ in range(n + 1)]
        
        for i in range(n - 1, -1, -1):
            for j in range(-1, i):
                if nums[i] > nums[j]:
                    LIS[i][j] = max(1 + LIS[i + 1][i], LIS[i + 1][j])
                else:
                    LIS[i][j] = LIS[i + 1][j]
        return LIS[0][-1]
        

