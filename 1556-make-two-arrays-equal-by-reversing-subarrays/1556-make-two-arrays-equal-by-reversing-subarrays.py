class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        hash_target = defaultdict(int)
        hash_arr = defaultdict(int)

        for i in target:
            hash_target[i] += 1
            
        for i in arr:
            hash_arr[i] += 1

        return True if hash_target == hash_arr else False
