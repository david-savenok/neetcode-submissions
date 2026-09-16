class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        letters = [0] * 26
        for c in s1:
            letters[ord(c) - ord('a')] += 1
        seen = [0] * 26
        l = r = 0
        while r < len(s2):
            print(seen, l, r)
            if letters[ord(s2[r]) - ord('a')] - seen[ord(s2[r]) - ord('a')] > 0:
                seen[ord(s2[r]) - ord('a')]  += 1
                if r - l + 1 == len(s1):
                    return True
                r += 1
            elif letters[ord(s2[r]) - ord('a')] == 0:
                r += 1
                l = r
                seen = [0] * 26
            else:
                while letters[ord(s2[r]) - ord('a')] - seen[ord(s2[r]) - ord('a')] <= 0:
                    seen[ord(s2[l]) - ord('a')] = max(0, seen[ord(s2[l]) - ord('a')] - 1) 
                    l += 1
                seen[ord(s2[r]) - ord('a')]  += 1
                if r - l + 1 == len(s1):
                    return True
                r += 1
        return False
