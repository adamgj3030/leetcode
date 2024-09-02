class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.right = ListNode(0)
        self.left = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left
        

    def get(self, index: int) -> int:
        currNode = self.left.next

        while currNode and index > 0:
            currNode = currNode.next
            index -= 1
        
        if currNode and (currNode != self.right) and (index == 0):
            return currNode.val

        return -1

    def addAtHead(self, val: int) -> None:
        node, next, prev = ListNode(val), self.left.next, self.left
        prev.next = node
        node.prev = prev
        node.next = next
        next.prev = node

    def addAtTail(self, val: int) -> None:
        node, next, prev = ListNode(val), self.right, self.right.prev
        prev.next = node
        node.prev = prev
        node.next = next
        next.prev = node

    def addAtIndex(self, index: int, val: int) -> None:
        currNode = self.left.next

        while currNode and index > 0:
            currNode = currNode.next
            index -= 1

        if currNode and index == 0:
            node, next, prev = ListNode(val), currNode, currNode.prev
            prev.next = node
            node.prev = prev
            node.next = next
            next.prev = node

    def deleteAtIndex(self, index: int) -> None:
        currNode = self.left.next

        currNode = self.left.next

        while currNode and index > 0:
            currNode = currNode.next
            index -= 1

        if currNode and (currNode != self.right) and index == 0:
            next, prev = currNode.next, currNode.prev
            prev.next = next
            next.prev = prev

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
