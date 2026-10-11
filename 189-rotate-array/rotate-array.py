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
        
        # from collections import deque

        # d = deque(nums)
        # d.rotate(k)
        # nums[:] = list(d)
        def reverse(nums,left,right):
            while left<right:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
                right-=1
        reverse(nums,n-k,n-1)
        reverse(nums,0,n-k-1)
        reverse(nums,0,n-1)


        