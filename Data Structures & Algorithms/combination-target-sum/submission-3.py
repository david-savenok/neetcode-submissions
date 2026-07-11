class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combo = []

        def _sum(i, target):
            if target <= 0:
                if target == 0:
                    res.append(combo.copy())
                return
            if i >= len(nums):
                return
            
            # add the element and recurse
            combo.append(nums[i])
            _sum(i, target - nums[i])

            # remove element and recurse
            combo.pop()
            _sum(i + 1, target)
        
        _sum(0, target)
        return res

