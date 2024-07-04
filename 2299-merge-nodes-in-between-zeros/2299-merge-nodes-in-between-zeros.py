# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
       
        modify = head.next
        nextsum = modify

        while nextsum:
            summ = 0
            while nextsum.val != 0:
                summ += nextsum.val
                nextsum = nextsum.next
            
            modify.val = summ

            nextsum = nextsum.next
            modify.next = nextsum
            modify = modify.next

        return head.next