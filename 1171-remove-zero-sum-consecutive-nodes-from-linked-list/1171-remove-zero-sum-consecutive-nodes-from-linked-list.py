# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        A, curr = [], head
        while curr:
            A.append(curr.val)
            curr = curr.next
        def isDelete(A):
            hashT, sum_ = {0: -1}, 0
            for i, num in enumerate(A):
                sum_ += num
                if 0-sum_ in hashT:
                    A = A[:hashT[0-sum_]+1] + A[i+1:]
                    return True, A
                hashT[-sum_] = i
            return False, A
        f = True
        while f:
            f, A = isDelete(A)
        ans = t = ListNode()
        for num in A:
            t.next = ListNode(num)
            t = t.next
        return ans.next