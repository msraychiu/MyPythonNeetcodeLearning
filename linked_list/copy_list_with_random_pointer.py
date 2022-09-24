"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        map = {None:None}
        cur = head
        while cur is not None:
            map[cur] = Node(cur.val, None, None)
            cur = cur.next

        cur = head
        while cur is not None:
            new_cur = map[cur]
            new_cur.next = map[cur.next]
            new_cur.random = map[cur.random]
            cur = cur.next

        return map[head]

