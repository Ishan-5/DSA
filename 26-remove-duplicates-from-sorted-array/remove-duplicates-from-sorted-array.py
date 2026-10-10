class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        frq_map={}
        for i in range (0,n):
            frq_map[nums[i]]=0
        j=0
        for k in frq_map:
            nums[j]=k
            j+=1
        return j