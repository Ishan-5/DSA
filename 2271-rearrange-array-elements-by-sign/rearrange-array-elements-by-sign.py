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
        # Create a result array filled with placeholders
        result = [0] * len(nums)
        
        # Pointers for tracking the next available slot
        pos_idx = 0
        neg_idx = 1
        
        for num in nums:
            if num > 0:
                result[pos_idx] = num
                pos_idx += 2  # Move to the next even index
            else:
                result[neg_idx] = num
                neg_idx += 2  # Move to the next odd index
                
        return result

