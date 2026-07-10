class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = 0
        groups = {}
        res = []
        for s in strs:
            letters = [0] * 26
            for c in s:
                letters[ord(c) - ord('a')] += 1
            letters = tuple(letters)
            if letters in groups.keys():
                res[groups[letters]].append(s)
            else:
                res.append([s])
                groups.update({letters : count})
                count += 1
        return res