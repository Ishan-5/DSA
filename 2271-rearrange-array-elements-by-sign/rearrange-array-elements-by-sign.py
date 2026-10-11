# class Solution:
#     def rearrangeArray(self, nums: list[int]) -> list[int]:
        # pos=[]
        # neg=[]
        # for i in range(0,len(nums)):
        #     if nums[i]>=0:
        #         pos.append(nums[i])
        # for i in range(0,len(nums)):
        #     if nums[i]<0:
        #         neg.append(nums[i])  
     
        # for i in range(0,len(pos)):
        #     nums[(2*i)]=pos[i]
        #     nums[(2*i)+1]=neg[i]
        # return nums
class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:

        result = [0] * len(nums)
        
        pos_idx = 0
        neg_idx = 1
        
        for num in nums:
            if num > 0:
                result[pos_idx] = num
                pos_idx += 2  
            else:
                result[neg_idx] = num
                neg_idx += 2  
        return result

