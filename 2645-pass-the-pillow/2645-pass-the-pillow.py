class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        
        full_rounds = time // (n-1)
        print(f'full rounds : {full_rounds}')
        
        remaining_time = time %(n-1)
        print(f'remaining time :{remaining_time}')
        
        if full_rounds%2 == 0:
            return 1+remaining_time
        else:
            return  n- remaining_time