class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total_drunk = numBottles
        empty = numBottles
        
        while empty >= numExchange:
            #exchange
            full = empty // numExchange
            get_back = empty % numExchange
            empty = full+get_back
            total_drunk += full    
                  
        return(total_drunk)