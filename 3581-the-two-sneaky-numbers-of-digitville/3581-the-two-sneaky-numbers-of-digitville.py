class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        res=[]
        count={}
        for i in nums:
            count[i] = count.get(i,0) + 1
            if count[i] == 2:
                res.append(i)
        return res