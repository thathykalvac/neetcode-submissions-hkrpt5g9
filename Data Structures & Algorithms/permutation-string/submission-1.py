class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def profile(s):
            d={}
            for n in s:
                if n in d:
                    d[n]+=1
                else:
                    d[n]=1
            return d
        s1d=profile(s1)
        s2d=profile(s2[:len(s1)])
        if s1d==s2d:
            return True
        for i in range(1,len(s2)-len(s1)+1):
            s2d[s2[i-1]]-=1
            if s2d[s2[i-1]]==0:
                del s2d[s2[i-1]]
            if s2[len(s1)+i-1] in s2d:
                s2d[s2[len(s1)+i-1]]+=1
            else:
                s2d[s2[len(s1)+i-1]]=1
            if s1d==s2d:
                return True
        return False



