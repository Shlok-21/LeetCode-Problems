class Solution:
    def findThePrefixCommonArray(self, a, b):
        ans =[]
        for i in range(1,len(a)+1):
            count=0
            for element in a[:i]:
                if element in b[:i]:
                    count+=1
            ans.append(count)
        return ans