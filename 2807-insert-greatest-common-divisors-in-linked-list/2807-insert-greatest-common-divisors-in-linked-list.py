# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        A = []
        while head:
            A.append(head.val)
            head = head.next
        ans = tail = ListNode(-1)
        for i in range(len(A)-1):
            tail.next = ListNode(A[i])
            tail = tail.next
            tail.next = ListNode(math.gcd(A[i], A[i+1]))
            tail = tail.next
        tail.next = ListNode(A[-1])
        return ans.next