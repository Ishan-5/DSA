class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        temp=[]
        for i in range (0,n):
            if nums[i]!=0:
                temp.append(nums[i])
        nt=len(temp)
        for i in range(0,nt):
            nums[i]=temp[i]
        for i in range(nt,n):
            nums[i]=0