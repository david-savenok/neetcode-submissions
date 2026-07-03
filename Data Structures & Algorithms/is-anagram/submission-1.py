class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        for c in s:
            if c in seen:
                seen[c] += 1
            else:
                seen.update({c : 1})
        for c in t:
            if c in seen:
                if seen[c] > 0:
                    seen[c] -= 1
                    if seen[c] == 0:
                        seen.pop(c)
                else:
                    return False
            else:
                return False
        return not seen
        