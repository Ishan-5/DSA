class Solution:
    def totalMoney(self, n: int) -> int:
        a = n // 7
        b = n % 7
        return 28*a + 7*a*(a-1)//2 + b*(a+1) + b*(b-1)//2