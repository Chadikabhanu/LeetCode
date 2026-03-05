class Solution:
    def minOperations(self, s: str) -> int:
            st0=0
            st1=0
            for i in range(len(s)):
                if i % 2 ==0:
                    if s[i] == "0":
                        st1+=1
                    else:
                        st0+=1
                else:
                    if s[i] == "1":
                        st1+=1
                    else:
                        st0+=1
            return min(st0,st1)