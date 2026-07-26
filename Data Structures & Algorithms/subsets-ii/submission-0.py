class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.curr = []

        def subsets(i):
            if i >= len(nums):
                sorted_set = sorted(self.curr.copy())
                if sorted_set not in self.res:
                    self.res.append(sorted_set)
                return

            self.curr.append(nums[i])
            subsets(i + 1)
            self.curr.pop()
            subsets(i + 1)
        
        subsets(0)
        return self.res
