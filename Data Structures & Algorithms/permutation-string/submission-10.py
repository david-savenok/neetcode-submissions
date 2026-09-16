class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        letters = [0] * 26
        for c in s1:
            letters[ord(c) - ord('a')] += 1
        seen = [0] * 26
        l = r = 0
        while r < len(s2):
            letter_count = letters[ord(s2[r]) - ord('a')]
            if letter_count == 0:
                r += 1
                l = r
                seen = [0] * 26
                continue
            else:
                while letter_count - seen[ord(s2[r]) - ord('a')] <= 0:
                    seen[ord(s2[l]) - ord('a')] = max(0, seen[ord(s2[l]) - ord('a')] - 1) 
                    l += 1
            seen[ord(s2[r]) - ord('a')] += 1
            if r - l + 1 == len(s1):
                return True
            r += 1
        return False
