class Solution:
    def rob(self, nums: List[int]) -> int:
        L = len(nums)
        HR = [0] * (L + 2) 

        for i in range(L - 1, -1, -1):
            HR[i] = max(nums[i] + HR[i + 2], HR[i + 1])

        return HR[0]