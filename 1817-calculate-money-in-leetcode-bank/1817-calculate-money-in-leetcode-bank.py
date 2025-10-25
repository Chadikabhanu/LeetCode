class Solution:
    def totalMoney(self, n: int) -> int:
        a=0
        mon=1
        while n > 0:
            for i in range(min(n,7)):
                a+=mon+i
            n-=7
            mon+=1
        return a
