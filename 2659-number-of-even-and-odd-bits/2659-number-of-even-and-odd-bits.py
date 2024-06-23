class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        binary = str(bin(n)[2:])[::-1]
        count_even = 0
        count_odd = 0
        print(type(binary))
        for i in range(len(binary)):
            if i%2 == 0 and binary[i] == '1':
                count_even +=1
            
            if i%2 == 1 and binary[i] == '1':
                count_odd +=1

        return([count_even, count_odd])