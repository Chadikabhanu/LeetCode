class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        f1 = [0] * 26
        for ch in s:
            f1[ord(ch) - ord('a')] += 1
        f2 = [0] * 26
        for ch in t:
            f2[ord(ch) - ord('a')]+=1
        for i in range(26):
            if f1[i] != f2[i]:
                return False
        return True

