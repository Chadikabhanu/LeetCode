class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        m=1
        nums.sort()
        for num in nums:
            if num > 0 and m == num:
                m+=1
        return m
