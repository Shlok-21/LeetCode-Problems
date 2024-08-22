class Solution:
    def findComplement(self, num: int):
        if num == 0:
            return 0
        binary = ''
        while num > 0:
            binary = str(num%2) + binary
            num = num // 2
        
        flipped=['1' if x == '0' else '0' for x in binary]                
        multi = 1
        summ = 0
        flipped = flipped[::-1]
        print(flipped)
        
        for i in range(len(flipped)):
            print(flipped[i])
            if flipped[i] == '1':
                summ += multi
            multi *= 2
            
        return (summ)
