class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.subset = []

        def _subsets(i):
            if i >= len(nums):
                self.res.append(self.subset.copy())
                return
            self.subset.append(nums[i])
            _subsets(i + 1)
            self.subset.pop()
            _subsets(i + 1)
        
        _subsets(0)
        return self.res