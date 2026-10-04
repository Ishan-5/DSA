class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n//7
        rem = n%7
        full_weeks_sum = weeks * 28 + 7 * (weeks * (weeks - 1)) // 2
        leftover_sum = rem * (weeks + 1) + (rem * (rem - 1)) // 2
        
        return full_weeks_sum + leftover_sum
