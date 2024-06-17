class Solution:
    def findIntersectionValues(self, nums1, nums2):
        count=0
        for i in nums1:
            if i in nums2:
                count+=1
        ar1 = [count]
        count=0
        for i in nums2:
            if i in nums1:
                count+=1
        ar1.append(count)
    
        return ar1