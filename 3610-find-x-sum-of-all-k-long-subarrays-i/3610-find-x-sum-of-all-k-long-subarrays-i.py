from collections import Counter

class Solution:
    def findXSum(self, nums, k, x):
        n = len(nums)
        ans = []
        for i in range(n - k + 1):
            sub = nums[i:i+k]
            freq = Counter(sub)
            sorted_items = sorted(freq.items(), key=lambda t: (-t[1], -t[0]))
            top_x = {val for val, _ in sorted_items[:x]}            
            total = sum(v for v in sub if v in top_x)
            ans.append(total)        
        return ans
