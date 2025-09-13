from collections import Counter
class Solution:
    def maxFreqSum(self, s: str) -> int:
        freq_map = Counter(s)
        vowels = "aeiouAEIOU"   
        max_vowel_freq = max(
            (freq_map[ch] for ch in freq_map if ch in vowels),
            default=0
        )
        max_consonant_freq = max(
            (freq_map[ch] for ch in freq_map if ch.isalpha() and ch not in vowels),
            default=0
        )
        return max_vowel_freq + max_consonant_freq
