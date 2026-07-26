class Solution:
    def rob(self, nums: List[int]) -> int:
        L = len(nums)
        skip, noskip, curr, res = 0, 0, 0, 0

        if L == 1:
            return nums[0]

        for i in range(L - 1, 0, -1):
            curr = max(nums[i] + skip, noskip)
            skip = noskip
            noskip = curr

        skip, noskip, curr, res = 0, 0, 0, curr
        for i in range(L - 2, -1, -1):  
            curr = max(nums[i] + skip, noskip)
            skip = noskip
            noskip = curr

        return max(res, curr)