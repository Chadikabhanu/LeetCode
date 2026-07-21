class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        missing=1
        nums.sort()
        for num in nums:
            if missing > 0 and missing == num:
                missing+=1
        return missing