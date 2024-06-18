class Solution:
    def uniqueOccurrences(self, arr) -> bool:
        uniques = {x : arr.count(x) for x in arr}
        check = [k for _, k in uniques.items()]
        return True if len(check) == len(set(check)) else False