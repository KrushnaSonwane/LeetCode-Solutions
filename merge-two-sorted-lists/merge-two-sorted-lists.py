# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        ans = tail = ListNode()
        def sol(l1, l2, ans, tail):
            if not l1 or not l2:
                if l2: tail.next = l2
                if l1: tail.next = l1
                return ans.next
            if l2.val > l1.val:
                tail.next = l1
                return sol(l1.next, l2, ans, tail.next)
            else:
                tail.next = l2
                return sol(l1, l2.next, ans, tail.next)
        return sol(l1, l2, ans, tail)
