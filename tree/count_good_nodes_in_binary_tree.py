# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.count(root, root.val)

    def count(self, node, parent_max):
        if not node:
            return 0

        if node.val >= parent_max:
            result = 1
        else:
            result = 0

        parent_max = max(parent_max, node.val)

        if node.left:
            result += self.count(node.left, parent_max)
        if node.right:
            result += self.count(node.right, parent_max)
        return result