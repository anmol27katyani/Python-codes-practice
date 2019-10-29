# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, s: int) -> bool:
        if not root:
            return False
        s -= root.val
        if s == 0 and not root.left and not root.right:
            return True
        return self.hasPathSum(root.left, s) or self.hasPathSum(root.right, s)