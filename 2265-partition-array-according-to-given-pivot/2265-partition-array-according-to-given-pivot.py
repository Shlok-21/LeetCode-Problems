class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        arr = [pivot]
        less, more, piv = [], [], []
        for i in nums:
            if i < pivot:
                less.append(i)
            elif i == pivot:
                piv.append(i)
            else:
                more.append(i)
        return(less+piv+more)