class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.curr = []

        def subsets(i):
            if i >= len(nums):
                self.res.append(self.curr.copy())
                return

            self.curr.append(nums[i])
            subsets(i + 1)
            self.curr.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            subsets(i + 1)
        
        nums.sort()
        subsets(0)
        return self.res
