# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        def rev(head):
            prev = None
            while head:
                curr = head
                nxt = head.next
                head.next = prev
                prev = head
                head = nxt
            return prev
        carry, head = 1, rev(head)
        res = tail = ListNode(-1)
        while head:
            val = head.val + carry
            tail.next = ListNode(val%10)
            tail = tail.next
            carry = val // 10
            head = head.next
        if carry:
            tail.next = ListNode(carry)
        return rev(res.next)