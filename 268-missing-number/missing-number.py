class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        
        # Calculate what the sum should be from 0 to n
        expected_sum = (n * (n + 1)) // 2
        
        # Calculate the actual sum of the numbers we have
        actual_sum = sum(nums)
        
        # The difference is the missing number
        return expected_sum - actual_sum
