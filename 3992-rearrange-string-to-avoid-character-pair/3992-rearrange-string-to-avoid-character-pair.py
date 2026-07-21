class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        xcount,ycount=[],[]
        others=[]
        for i in s:
            if i == x:
                xcount.append(i)
            elif i == y:
                ycount.append(i)
            else:
                others.append(i)
        return "".join(ycount+others+xcount)
