# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find middle
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # reverse second half
        prev, curr = None, slow
        while curr:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
        
        # merge first and reversed second half of list
        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
