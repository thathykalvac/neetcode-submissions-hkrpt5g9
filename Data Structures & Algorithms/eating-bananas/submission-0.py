import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        res=r
        while l<=r:
            a=(l+r)//2
            th=0
            for n in piles:
                th+=math.ceil(n/a)
            if th<=h:
                res=min(res,a)
                r=a-1
            else:
                l=a+1
        return res
            
        