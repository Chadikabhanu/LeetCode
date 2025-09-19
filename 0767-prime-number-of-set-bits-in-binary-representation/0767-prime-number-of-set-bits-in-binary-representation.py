class Solution(object):
    def countPrimeSetBits(self, L, R):
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        count = 0
        for x in range(L, R + 1):
            set_bits = bin(x).count('1')
            if set_bits in primes:
                count += 1
        return count
