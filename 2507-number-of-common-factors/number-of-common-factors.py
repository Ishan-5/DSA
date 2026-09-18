class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        import math
        gcd_num=math.gcd(a,b)
        count=0
        for i in range(1, int(math.sqrt(gcd_num)) + 1):
            if gcd_num % i == 0:
                count += 1            
                if i * i != gcd_num:
                    count += 1        
                    
        return count


        

