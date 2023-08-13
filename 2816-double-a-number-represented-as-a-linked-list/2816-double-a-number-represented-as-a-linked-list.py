# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        temp = head
        while temp:
            res.append(temp.val)
            temp = temp.next
        i = len(res)-1
        res = res[::-1]
        carry = 0
        for i, num in enumerate(res):
            curr = num * 2
            curr += carry
            res[i] = curr % 10
            carry = curr // 10
        res = res[::-1]
        ans = tail = ListNode(-1)
        if carry:
            tail.next = ListNode(carry)
            tail = tail.next
        for ch in res:
            tail.next = ListNode(ch)
            tail = tail.next
        return ans.next