from typing import List

def merge_sort(nums):
    n = len(nums)
    if n <= 1:
        return
    
    mid_ind = int(n//2)
    left_arr : List[int] = nums[:mid_ind]
    right_arr : List[int] = nums[mid_ind:]
    
    merge_sort(left_arr)
    merge_sort(right_arr)
    merge(left_arr, right_arr, nums)
    
    
def merge(array1, array2, source_array):
    p1 = 0
    p2 = 0
    
    n1 = len(array1)
    n2 = len(array2)
    
    write_ind = 0

    while p1 < n1 or p2 < n2:
        if p1 == n1 or (p2 != n2 and array2[p2] < array1[p1]):
            source_array[write_ind] = array2[p2]
            p2 += 1
        elif p2 == n2 or array1[p1] <= array2[p2]:
            source_array[write_ind] = array1[p1]
            p1 += 1
        write_ind += 1


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        merge_sort(nums)
        return nums