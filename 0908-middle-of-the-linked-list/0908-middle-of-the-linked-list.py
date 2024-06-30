# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slowpointer = head
        fastpointer = head

        while fastpointer is not None and fastpointer.next is not None:
            slowpointer = slowpointer.next
            fastpointer = fastpointer.next.next

        return slowpointer
