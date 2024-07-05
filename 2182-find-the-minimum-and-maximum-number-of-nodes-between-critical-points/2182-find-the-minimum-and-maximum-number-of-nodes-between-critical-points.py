# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        left = head
        mid = head.next
        right = mid.next

        curr_index = 2
        indexes = []

        while right:
            # Check if the center value is a critical point
            if (mid.val > left.val and mid.val > right.val) or (mid.val < left.val and mid.val < right.val):
                # append the index if it is critical
                indexes.append(curr_index)

                # increments
            curr_index += 1
            left = mid
            mid = right
            right = right.next
        
        if len(indexes) < 2:
            return [-1,-1]

        print(indexes)
        #check if we found any critical points
        max_dist = max(indexes) - min(indexes)
        
        min_dist = max(indexes)
        for i in range(len(indexes)-1):
            if (indexes[i+1] - indexes[i]) < min_dist:
                min_dist = (indexes[i+1] - indexes[i])
        
        return [min_dist, max_dist]
        