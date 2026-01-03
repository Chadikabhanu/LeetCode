class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        count=collections.Counter(nums)
        for n in count:
            if count[n] > 1:
                return n
