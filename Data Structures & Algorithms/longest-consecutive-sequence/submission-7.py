class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        next_seq = {}
        max_seq = 0
        seen = {}

        for num in nums:
            next_seq[num] = num + 1
        
        for num in nums:
            if num not in seen:
                curr = num
                count = 1
                while next_seq[curr] in next_seq:
                    if next_seq[curr] not in seen:
                        count += 1
                        curr = next_seq[curr]
                    else:
                        count += seen[next_seq[curr]]
                        break
                max_seq = max(count, max_seq)
                seen[num] = count
        return max_seq