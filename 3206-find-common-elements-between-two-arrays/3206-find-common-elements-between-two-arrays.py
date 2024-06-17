class Solution:
    def findIntersectionValues(self, nums1, nums2):
        check1 = set(nums1)
        check2 = set(nums2)
        count1 = count2 = 0
        
        for i in nums1:
            if i in check2:
                count1 +=1
        for i in nums2:
            if i in check1:
                count2 +=1
        return[count1,count2]