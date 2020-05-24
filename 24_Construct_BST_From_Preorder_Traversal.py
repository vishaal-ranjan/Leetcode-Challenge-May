# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        index = [0]
        constraint = 2**31 - 1
        return self.helper(index, preorder, constraint)
    
    def helper(self, index, preorder, constraint):
        tree = TreeNode(preorder[index[0]])
        print(tree)
        index[0] += 1
        if index[0] < len(preorder) and preorder[index[0]] < tree.val:
            tree.left = self.helper(index, preorder, tree.val)
        if index[0] < len(preorder) and preorder[index[0]] < constraint:
            tree.right = self.helper(index, preorder, constraint)
        return tree