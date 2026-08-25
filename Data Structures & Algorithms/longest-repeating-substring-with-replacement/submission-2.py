class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        l = r = 0
        freq = [0] * 26
        maxf = 0
        while r < len(s):
            freq[ord(s[r]) - ord('A')] += 1
            maxf = max(maxf, freq[ord(s[r]) - ord('A')])
            if (r - l + 1) - maxf > k:
                freq[ord(s[l]) - ord('A')] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)
            r += 1
        return max_len

