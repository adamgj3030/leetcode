# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        stack, visit = [root], [False]

        while stack:
            cur, visited = stack.pop(), visit.pop()
            if visited:
                res.append(cur.val)
            else:
                stack.append(cur)
                visit.append(True)
                if cur.right:
                    stack.append(cur.right)
                    visit.append(False)
                if cur.left:
                    stack.append(cur.left)
                    visit.append(False)
        
        return res
