# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur is not None:
           #store the next element and set a new next to current
           next_node = cur.next
           cur.next = prev
           #shift to next
           prev = cur
           cur = next_node
        return cur
