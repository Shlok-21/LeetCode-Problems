class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        if nums1[0] > nums2[0]:
            return -(nums1[0] - nums2[0])
        else:
            return nums2[0] - nums1[0]
