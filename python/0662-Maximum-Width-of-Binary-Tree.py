# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque([(root, 0)])
        res = 1

        while queue:
            level_size = len(queue)
            left_pos = queue[0][1]
            right_pos = queue[-1][1]

            for _ in range(level_size):
                node, pos = queue.popleft()

                if node.left:
                    queue.append((node.left, pos * 2))
                if node.right:
                    queue.append((node.right, pos * 2 + 1))
            
            res = max(res, right_pos - left_pos + 1)
        
        return res
            
