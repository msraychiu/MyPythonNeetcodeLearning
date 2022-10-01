# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        head = res
        carry = 0
        while l1 is not None and l2 is not None:
            temp = l1.val + l2.val + carry
            sum = 0
            if temp >= 10:
                carry = 1
                sum = temp % 10
            else:
                carry = 0
                sum = temp

            res.next = ListNode(sum, None)

            l1 = l1.next
            l2 = l2.next
            res = res.next

        while l1 is not None:
            temp = (l1.val + carry)
            sum = 0
            if temp >= 10:
                carry = 1
                sum = temp % 10
            else:
                carry = 0
                sum = temp
            res.next = ListNode(sum, None)
            l1 = l1.next
            res = res.next

        while l2 is not None:
            temp = (l2.val + carry)
            sum = 0
            if temp >= 10:
                carry = 1
                sum = temp % 10
            else:
                carry = 0
                sum = temp
            res.next = ListNode(sum, None)
            l2 = l2.next
            res = res.next

        if carry > 0:
            res.next = ListNode(1, None)

        return head.next
