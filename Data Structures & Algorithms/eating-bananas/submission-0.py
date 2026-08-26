class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hoursToEat(m, p):
            total = 0
            for pile in p:
                total += math.ceil(pile / m)
            return total

        l = 1
        r = max(piles)
        mink = r

        while l <= r:
            mid = (l + r) // 2
            
            if hoursToEat(mid, piles) <= h:
                mink = min(mink, mid)
                r = mid - 1
            else:
                l = mid + 1
                
        return mink
