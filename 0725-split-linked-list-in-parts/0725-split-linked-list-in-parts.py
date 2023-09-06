# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n, t = 0, head
        while t:
            n += 1
            t = t.next
        res, m = [], n // k
        extra = n-m*k
        for _ in range(k):
            ans = tail = ListNode()
            for _ in range(m):
                tail.next = ListNode(head.val)
                tail = tail.next
                head = head.next
            if extra:
                tail.next = ListNode(head.val)
                tail = tail.next
                head = head.next
                extra -= 1
            res.append(ans.next)
        return res