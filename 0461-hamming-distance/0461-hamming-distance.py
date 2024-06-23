class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        binx = []
        biny = []

        while x>1:
            rem = x%2
            binx.append(int(rem))
            x/=2
        else:
            binx.append(int(x))
        
        while y>1:
            rem = y%2
            biny.append(int(rem))
            y/=2
        else:
            biny.append(int(y))      

        while len(binx) > len(biny):
            biny.append(0)
        while len(biny) > len(binx):
            binx.append(0)
        count = 0
        for i in range(len(binx)):
            if binx[i] != biny[i]:
                count +=1
        return count