class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sn=set(nums)
        c=0
        for i in nums:
            temp=i
            tempc=1
            while temp+1 in sn:
                temp+=1
                tempc+=1
            if tempc>c:
                c=tempc
        return c

        