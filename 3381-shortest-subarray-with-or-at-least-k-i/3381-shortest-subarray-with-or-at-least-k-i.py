class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        bitCount = [0] * 32
        def add(num):
            for b in range(32):
                if num & (1 << b):
                    bitCount[b] += 1
        def remove(num):
            for b in range(32):
                if num & (1 << b):
                    bitCount[b] -= 1
        def currentOR():
            val = 0
            for b in range(32):
                if bitCount[b] > 0:
                    val |= (1 << b)
            return val
        ans = float('inf')
        l = 0
        for r in range(n):
            add(nums[r])
            while l <= r and currentOR() >= k:
                ans = min(ans, r - l + 1)
                remove(nums[l])
                l += 1
        return ans if ans != float('inf') else -1