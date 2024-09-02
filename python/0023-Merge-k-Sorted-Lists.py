# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedList = []

            for i in range(0, len(lists), 2):
                list1 = lists[i]
                nexti = i + 1
                if nexti < len(lists):
                    list2 = lists[nexti]
                    mergedList.append(self.mergeLists(list1, list2))
                else:
                    mergedList.append(list1)
            
            lists = mergedList
        
        return lists[0]
        
    def mergeLists(self, list1, list2):
        currNode = res = ListNode()

        while list1 and list2:
            if list1.val <= list2.val:
                currNode.next = list1
                list1 = list1.next
            else:
                currNode.next = list2
                list2 = list2.next
            currNode = currNode.next

        if list1:
            currNode.next = list1
        elif list2:
            currNode.next = list2

        return res.next
