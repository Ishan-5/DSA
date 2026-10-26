class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merge=sorted(nums1+nums2)
        medi=0.00
        mid=len(merge)//2
        if len(merge)%2==0:
            medi= (merge[mid]+merge[mid-1])/2
        else:
            medi=merge[mid]
        return medi
        
        medi=merge[mid]
        return medi
                  