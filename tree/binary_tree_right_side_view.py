# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = []
        result = [root.val]
        if root.left:
            q.append(root.left)
        if root.right:
            q.append(root.right)

        while q:
            tmp = []
            for node in q:
                if node and node.left:
                    tmp.append(node.left)
                if node and node.right:
                    tmp.append(node.right)
            q_pop = q.pop()
            result.append(q_pop.val)
            q = tmp

        return result