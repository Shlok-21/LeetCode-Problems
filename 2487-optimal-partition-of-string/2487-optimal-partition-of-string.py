class Solution:
    def partitionString(self, string: str) -> int:
        temp = ''
        subs =[]
        for char in string:
            if char in temp:
                subs.append(temp)
                temp = char
            else:
                temp+=char
                
        if temp: subs.append(temp)
        
        return len(subs)