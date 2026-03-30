class Solution:
    def isValid(self, s: str) -> bool:
        lp=0
        rp=len(s)-1
        p={"(","{","["}
        dp={")":"(",
        "}":"{",
        "]":"[",
        }
        l=[]
        for n in s:
            if n in p:
                l.append(n)
            elif n in dp:
                if not l or l.pop() != dp[n]:
                    return False
        return not l


        