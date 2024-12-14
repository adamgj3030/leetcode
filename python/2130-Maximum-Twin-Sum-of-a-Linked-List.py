# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        curSum = 0
        curMax = -1
        prev = None

        while fast:
            fast = fast.next.next
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        first = prev
        second = slow
        while second:
            curSum = first.val + second.val
            curMax = max(curMax, curSum)
            first = first.next
            second = second.next
        return curMax
