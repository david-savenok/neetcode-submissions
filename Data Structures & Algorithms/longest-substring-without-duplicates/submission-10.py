class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        length = 0
        l = 0
        r = 0
        while r < len(s):
            if s[r] in seen:
                l = max(seen[s[r]] + 1, l)
            seen[s[r]] = r
            length = max(length, r - l + 1)
            r += 1
        return length