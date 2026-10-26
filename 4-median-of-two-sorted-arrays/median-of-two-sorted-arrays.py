class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Ensure nums1 is the smaller array to minimize the binary search range
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        total_left = (m + n + 1) // 2
        
        while low <= high:
            partition1 = (low + high) // 2
            partition2 = total_left - partition1
            
            # Edges cases handled with infinity when partition falls outside array bounds
            max_left1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            min_right1 = float('inf') if partition1 == m else nums1[partition1]
            
            max_left2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            min_right2 = float('inf') if partition2 == n else nums2[partition2]
            
            # Check if partition is correct
            if max_left1 <= min_right2 and max_left2 <= min_right1:
                # If total length is odd, the median is the max of the left partition
                if (m + n) % 2 == 1:
                    return float(max(max_left1, max_left2))
                # If total length is even, it's the average of the two middle elements
                else:
                    return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2.0
            
            # Adjust binary search window
            elif max_left1 > min_right2:
                high = partition1 - 1
            else:
                low = partition1 + 1
                
        return 0.0
