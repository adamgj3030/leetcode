# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        if not head:
            return None
        prev = dummy = ListNode(val = 0, next = head)
        left, right = head, head.next
        while right:
            _next = right.next
            prev.next = right
            right.next = left
            left.next = _next
            if not _next:
                break
            prev = left
            left, right = _next, _next.next

        return dummy.next
