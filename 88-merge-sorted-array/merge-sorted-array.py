class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        result = []
        
        # 1. Merge elements into 'result' up to their active lengths (m and n)
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1
                
        # 2. Append any leftover elements from nums1
        while i < m:
            result.append(nums1[i])
            i += 1
            
        # 3. Append any leftover elements from nums2
        while j < n:
            result.append(nums2[j])
            j += 1
            
        # 4. CRITICAL STEP: Copy the elements from 'result' back into 'nums1' in-place
        for k in range(len(result)):
            nums1[k] = result[k]
