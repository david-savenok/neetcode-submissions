class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []

        def _permute(perm):
            if len(perm) == 1:
                curr.append(perm[0])
                res.append(curr.copy())
                curr.pop()
                return
            for i in range(len(perm)):
                temp = perm[i]
                curr.append(perm[i])
                perm.pop(i)
                _permute(perm)
                perm.insert(i, temp)
                curr.pop()
                

        _permute(nums)
        return res

