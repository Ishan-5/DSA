class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        hash_map={}
        n = len(nums)
        for i in range (0,n):
            hash_map[nums[i]] = hash_map.get(nums[i],0)+1
            if hash_map[nums[i]] >= n/2 :
                return nums[i]
