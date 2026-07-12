class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        combo = []
        candidates = sorted(candidates)

        def _comboSum(i, target):
            if target == 0:
                res.append(combo.copy())
                return
            if i >= len(candidates) or target < 0:
                return
            
            # select the current element
            combo.append(candidates[i])
            _comboSum(i + 1, target - candidates[i])

            # don't select current element
            combo.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            _comboSum(i + 1, target)

        _comboSum(0, target)
        return res