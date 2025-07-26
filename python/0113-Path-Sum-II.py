# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths = []
        def dfs(node: Optional[TreeNode], targetSum: int, curPath: List[int]) -> None:
            if not node:
                return

            curPath.append(node.val)
            targetSum -= node.val
            if targetSum == 0 and (not node.left and not node.right):
                nonlocal paths
                paths.append(curPath.copy())
            
            dfs(node.left, targetSum, curPath)
            dfs(node.right, targetSum, curPath)

            curPath.pop()

            return

        dfs(root, targetSum, [])

        return paths
