class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digit_sum=0
        digit_pro=1
        for ch in str(n):
            digit=int(ch)
            digit_sum+=digit
            digit_pro*=digit
        total=digit_sum+digit_pro
        return n % total ==0