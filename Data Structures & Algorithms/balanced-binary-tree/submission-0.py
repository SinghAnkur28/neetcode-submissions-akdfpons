# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        wh = True

        def dfs(node):
            nonlocal wh
            if not node:
                return [True, 0]
            
            left = dfs(node.left)
            right = dfs(node.right)

            wh = left[0] and right[0] and abs(left[1]-right[1]) <= 1
            return [wh, 1+max(left[1],right[1])]
        dfs(root)
        return wh
        