class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if mid - 1 >= 0 and nums[mid] < nums[mid - 1]:
                return nums[mid]
            elif nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        return nums[l]