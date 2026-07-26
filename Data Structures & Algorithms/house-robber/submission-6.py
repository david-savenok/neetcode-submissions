class Solution:
    def rob(self, nums: List[int]) -> int:
        L = len(nums)
        noskip = 0
        skip = 0
        curr = 0

        for i in range(L - 1, -1, -1):
            curr = max(nums[i] + skip, noskip)
            skip = noskip
            noskip = curr

        return curr