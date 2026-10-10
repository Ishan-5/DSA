class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # n = len(nums)
        # frq_map={}
        # for i in range (0,n):
        #     frq_map[nums[i]]=0
        # j=0
        # for k in frq_map:
        #     nums[j]=k
        #     j+=1
        # return j
        if not nums :
            return 0
        n = len(nums)
        i=0
        for j in range(1, n):
            if nums[i] != nums[j]:  
                i += 1              
                nums[i] = nums[j]   
                
        return i + 1 

