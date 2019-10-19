# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        v=root.val
        def dfs(root):
            if root is None:
                return
            p=dfs(root.left)
            x=root.val
            if x!=v:
                return False
            q=dfs(root.right)
            if p==False or q==False:
                return False
            else:
                return True
        u=inorder(root)
        return u