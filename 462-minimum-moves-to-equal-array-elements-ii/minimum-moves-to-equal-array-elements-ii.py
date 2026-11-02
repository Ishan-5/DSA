# class Solution:
#     def minMoves2(self, nums: List[int]) -> int:
#         nums.sort()  # Step 1: Sort the array
#         median = nums[len(nums) >> 1]  # Step 2: Find the middle element
#         return sum(abs(num - median) for num in nums)  # Step 3 & 4: Sum absolute differences
class Solution(object):
    def minMoves2(self, nums):
        nums.sort()
        median = nums[len(nums) // 2]
        return sum(abs(num - median) for num in nums)