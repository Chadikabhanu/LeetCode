class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return -1
        else:
            mn=min(nums)
            mx=max(nums)
            for num in nums:
                if num!=mn and num != mx:
                    return num
            return -1
