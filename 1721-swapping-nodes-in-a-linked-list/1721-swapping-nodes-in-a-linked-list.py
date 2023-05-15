# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        first = head
        fast = head
        for _ in range(k - 1):
            first = first.next
            fast = fast.next
        second = head
        while fast.next:
            fast = fast.next
            second = second.next
        first.val, second.val = second.val, first.val
        return head
        