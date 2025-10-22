class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = inf
        for left in range(n):
            temp = 0
            for right in range(left,n):
                temp |= nums[right]
                if temp>=k:
                    ans = min(ans,right-left+1)
                    break
        return ans if ans!=inf else -1