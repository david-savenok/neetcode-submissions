class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#"
            res += s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        j = i
        while i < len(s):
            while s[j] != "#":
                j += 1

            length = int(s[i : j])
            i = j + 1
            res.append(s[i : i + length])
            i += length 
            j = i
        return res
