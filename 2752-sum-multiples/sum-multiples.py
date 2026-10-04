class Solution:
    def sumOfMultiples(self, n: int) -> int:
        # Helper function to find the sum of multiples of 'k' up to 'n'
        def sum_k(k):
            count = n // k
            return k * (count * (count + 1)) // 2
            
        return (sum_k(3) + sum_k(5) + sum_k(7) 
                - sum_k(15) - sum_k(21) - sum_k(35) 
                + sum_k(105))