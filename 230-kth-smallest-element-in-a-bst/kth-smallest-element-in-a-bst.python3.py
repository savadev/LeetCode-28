# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        res = []
        def inner(node):
            if not node:
                return
            inner(node.left)
            res.append(node.val)
            inner(node.right)
        inner(root)
        return res[k-1]
            
        
        