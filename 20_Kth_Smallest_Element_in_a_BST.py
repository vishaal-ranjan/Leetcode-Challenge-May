# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k = k
        self.ans = None
        self.traverse(root)
        return self.ans
        
    def traverse(self, root: TreeNode):
        if not root:
            return
        self.traverse(root.left)
        self.k -= 1
        if self.k == 0:
            self.ans = root.val
            return
        self.traverse(root.right)