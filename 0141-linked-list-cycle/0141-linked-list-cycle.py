# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashT = set()
        while head and head not in hashT:
            hashT.add(head)
            head = head.next
        return head != None