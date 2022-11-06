# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        p_list = [p]
        q_list = [q]

        while p_list and q_list:
            p_pop = p_list.pop()
            q_pop = q_list.pop()

            if (p_pop and q_pop and p_pop.val != q_pop.val) or (type(p_pop) != type(q_pop)):
                return False

            if p_pop and q_pop:
                p_list.append(p_pop.left)
                p_list.append(p_pop.right)
                q_list.append(q_pop.left)
                q_list.append(q_pop.right)

        return True
