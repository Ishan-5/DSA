class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        from math import sqrt
        if num <= 1:
            return False
        result=[]
        for i in range (1, int(sqrt(num))+1):
            if num%i ==0:
                result.append(i)
                if num//i !=i:
                    result.append(num//i)
        result.remove(num)
        total = sum(result)
        if total == num:
            return True
        else :
            return False