# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = [[root.val]]
        q = []
        if root.left:
            q.append(root.left)
        if root.right:
            q.append(root.right)

        while q:
            tmp = []
            next = []
            for node in q:
                tmp.append(node.val)
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)

            q = next

            result.append(tmp)

        return result