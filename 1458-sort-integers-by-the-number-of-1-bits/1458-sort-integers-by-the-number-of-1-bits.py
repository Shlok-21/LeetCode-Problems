class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        hashmap = defaultdict(list)
        arr.sort()
        for i in range(len(arr)):
            countt = (bin(arr[i]))[2:]
            print(countt)
            countt = countt.count('1')
            print(countt)
            hashmap[countt].append(arr[i])
        
        hashmap_new = {key: hashmap[key] for key in sorted(hashmap.keys())}
        print(hashmap_new)

        ans = []
        for val in hashmap_new.values():
            ans =  ans+ [x for x in val]
        return(ans)