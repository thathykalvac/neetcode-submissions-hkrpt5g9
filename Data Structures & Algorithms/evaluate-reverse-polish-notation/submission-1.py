class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops={
            "+": lambda a,b: a+b,
            "-": lambda a,b: a-b,
            "*": lambda a,b: a*b,
            "/": lambda a,b: int(a/b)
        }
        l=[]
        for t in tokens:
            if t in ops:
                b,a=l.pop(), l.pop()
                l.append(ops[t](a,b))
            else:
                l.append(int(t))
        return l[0]
        
        