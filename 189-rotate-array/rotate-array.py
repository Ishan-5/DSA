class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k = k % n
        # nums[:] = nums[-k:] + nums[:-k]
        # for _ in range(0,k):
        #     e = nums.pop()
        #     nums.insert(0,e)
        from collections import deque

        d = deque(nums)
        d.rotate(k)
        nums[:] = list(d)


        