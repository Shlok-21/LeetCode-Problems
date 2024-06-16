class Solution:
    def sortSentence(self, s: str) -> str:
        arr = [i[-1] + i[:-1] for i in s.split()]
        arr.sort()
        for i in range(len(arr)):
            arr[i] = arr[i][1:]
        return ' '.join(arr)