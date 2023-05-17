# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        rev = slow
        nextN = None
        while rev:
            nextNN = rev.next
            rev.next = nextN
            nextN = rev
            rev = nextNN
        rev = nextN
        first, res = head, 0
        while rev:
            res = max(res, rev.val + first.val)
            first = first.next
            rev = rev.next
        return res