class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res=0
        n=len(nums)
        a=n*(n+1)//2
        for i in nums:
            res+=i
            c=a-res
        return c


        