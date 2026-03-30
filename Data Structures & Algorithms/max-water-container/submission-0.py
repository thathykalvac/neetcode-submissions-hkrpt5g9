class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lp=0
        rp=len(heights)-1
        vol=0
        while rp>lp:
            v=(rp-lp)*min(heights[lp],heights[rp])
            if v>vol:
                vol=v
            if heights[lp]>heights[rp]:
                rp-=1
            else:
                lp+=1
        return vol
        