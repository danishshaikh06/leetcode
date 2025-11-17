from typing import List

class Solution:
    def sort_array(self, nums1: List[int], nums2: List[int]) -> None:
        i = len(nums1) - 1
        j = 0

        # Swap elements that are out of order between nums1 and nums2
        while i >= 0 and j < len(nums2):
            if nums1[i] > nums2[j] and nums1[i] != nums2[j]:
                nums1[i], nums2[j] = nums2[j], nums1[i]
            i -= 1
            j += 1

        # Sort both arrays after swaps
        nums1.sort()
        nums2.sort()

        
        print(nums1 + nums2)

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]

Solution().sort_array(nums1, nums2)
