from typing import List

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def countones(x):
            c = 0
            while x:
                x &= x - 1  
                c += 1
            return c
        return sorted(arr, key=lambda x: (countones(x), x))