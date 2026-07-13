class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = nums.copy()
        for i in range(len(nums) - 2, -1, -1):
            nums[i] *= nums[i + 1]
        print(nums)
        
        product = 1
        nums.append(1)
        for i in range(len(nums) - 1):
            temp = res[i]
            res[i] = product * nums[i + 1]
            product *= temp

        return res