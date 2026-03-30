class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1={}
        d2={}
        for a in s:
            if a in d1:
                d1[a]+=1
            else:
                d1[a]=1
        for b in t:
            if b in d2:
                d2[b]+=1
            else:
                d2[b]=1
        return d1==d2
