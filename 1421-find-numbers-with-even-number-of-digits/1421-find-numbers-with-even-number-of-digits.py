import math
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        l=[]
        count=0
        for i in nums:
            l.append(floor(math.log10(i))+1)
        for j in l:
            if j % 2==0:
                count+=1
        return count
                    