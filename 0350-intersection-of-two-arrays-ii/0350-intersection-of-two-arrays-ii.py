class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []

        n1 = len(nums1)
        n2 = len(nums2)
        if n1>n2:
            big = nums1
            small = nums2
        else:
            big = nums2
            small = nums1

        for i in small:
            if i in big:
                ans.append(i)
                big.remove(i)
        return(ans)