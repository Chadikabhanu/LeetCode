class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        cur=0
        res=[]
        for i in nums:
            cur = (cur << 1) + i
            res.append(cur % 5 == 0)
        return res