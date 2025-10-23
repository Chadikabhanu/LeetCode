class Solution:
    def hasSameDigits(self, s: str) -> bool:
        n=len(s)
        o_list=list(s)
        for i in range(1,n-1):
            for j in range(n-i):
                digit1=ord(o_list[j]) - ord("0")
                digit2=ord(o_list[j+1]) - ord("0")
                o_list[j] = chr(((digit1+digit2) % 10) + ord("o"))
        return o_list[0] == o_list[1]