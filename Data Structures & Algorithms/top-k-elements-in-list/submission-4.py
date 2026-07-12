class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq.keys():
                freq[num] += 1
            else:
                freq[num] = 0

        freqs = [[] for i in range(len(nums) + 1)]
        for item in freq.items():
            freqs[item[1]].append(item[0])

        res = []
        for i in range(len(nums), -1, -1):
            if k <= 0:
                break
    
            res.extend(freqs[i])
            k -= len(freqs[i])

        return res