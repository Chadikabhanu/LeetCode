from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zerocount = 0
        longestwindow = 0
        start = 0
        
        for i in range(len(nums)):
            zerocount += (nums[i] == 0)   
            while zerocount > 1:          
                zerocount -= (nums[start] == 0)
                start += 1
            longestwindow = max(longestwindow, i - start)
        
        return longestwindow
