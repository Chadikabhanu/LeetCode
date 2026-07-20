from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        a=len(nums) // 2
        return nums[a]