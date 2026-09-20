class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
            
        from math import sqrt
        total = 0 
        
        for i in range(1, int(sqrt(num)) + 1):
            if num % i == 0:
                total += i
                if num // i != i:
                    total += num // i
                    
        return (total - num) == num