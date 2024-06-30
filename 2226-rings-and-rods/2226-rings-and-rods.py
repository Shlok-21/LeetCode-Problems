class Solution:
    def countPoints(self, rings: str) -> int:
        n = len(rings)
        if n < 6:
            return 0
        
        order = [rings[i:i+2] for i in range(0, n, 2)]
    
        hashmap = defaultdict(list)
        for i in range(len(order)):
            hashmap[order[i][1]].append(order[i][0])
        
        count = 0
        for value in hashmap.values():
            if len(set(value)) == 3:
                count +=1
                
        return(count)
        