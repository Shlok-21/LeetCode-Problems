class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        hashmap = defaultdict(int) 

        for i in sorted(items1+items2):
            key, value = i[0], i[1]
            hashmap[key] += value
        
        '''ans = []
        for key, val in hashmap.items():
            ans.append([key,val])
        print(ans)'''
        
        return [[key, val] for key, val in hashmap.items()]    
 