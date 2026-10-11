class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        # count =0
        # max_count = 0
        # for i in range(0,len(nums)):
        #     if nums[i]==1:
        #         count+=1
        #     else:
        #         if count > max_count:
        #             max_count=count
        #         count=0
        # return max(max_count,count)
        max=0
        temp=0
        for i in nums:
            if i==1:
                temp+=1
            else:
                if temp>max:
                    max=temp
                temp=0
        if temp>max:
                    max=temp       
        return max