class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        piles.sort()
        while left < right:
            mid = (left+right)//2
            count = 0
            for pile in piles:
                if pile%mid == 0:
                    count += pile//mid
                else:
                    count += pile//mid +1
            if count <= h:
                right = mid
            else:
                left = mid+1
        return right
