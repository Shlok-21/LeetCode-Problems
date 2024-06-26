# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        summ = []

        def inorder(root):
            if root == None: return
            inorder(root.left)
            if root.val >= low and root.val <= high:
                summ.append(root.val)
            inorder(root.right)

        inorder(root)
        return sum(summ)