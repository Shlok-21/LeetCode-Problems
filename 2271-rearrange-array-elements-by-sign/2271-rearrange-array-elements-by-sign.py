class Solution:
    def rearrangeArray(self, nums):
        pos = []
        neg = []
        for i in nums:
            if i>=0:
                pos.append(i)
            else:
                neg.append(i)
        res = []
        for index in range(len(pos)):
            res.append(pos[index])
            res.append(neg[index])
        return(res)