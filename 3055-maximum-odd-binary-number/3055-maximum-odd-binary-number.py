class Solution:
    def maximumOddBinaryNumber(self, s):
        #dic = {x : s.count(x) for x in s}
        #return (dic.get('1',1) -1)*'1' +dic.get('0',0)*'0'+'1'
        return ''.join(sorted(s))[:len(s)-1][::-1]+'1'
