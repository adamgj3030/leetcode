# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        cur = root
        while cur:
            if not cur.left:
                res.append(cur.val)
                cur = cur.right
            else:
                pred = cur.left
                while pred.right and (pred.right is not cur):
                    pred = pred.right
                
                if pred.right is cur:
                    pred.right = None
                    cur = cur.right
                else:
                    pred.right = cur
                    res.append(cur.val)
                    cur = cur.left
        
        return res
