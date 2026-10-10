class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        
        values = sorted(set(nums), reverse=True)

        return values[2] if len(values) >= 3 else values[0]