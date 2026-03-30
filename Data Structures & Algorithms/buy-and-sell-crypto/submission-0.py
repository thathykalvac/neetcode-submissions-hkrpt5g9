class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min=prices[0]
        p=0
        for n in prices:
            tp=n-min
            if tp>p:
                p=tp
            if min>n:
                min=n
        return p



