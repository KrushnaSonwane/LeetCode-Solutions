# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a, b, sum_ = 0, 0, 0
        while l1 or l2:
            if l1:
                a = (a * 10) + l1.val
                l1 = l1.next
            if l2:
                b = (b * 10) + l2.val
                l2 = l2.next
                
        sum_ = str(a + b)
        sum_ = sum_[::-1]
        sumList = []
        
        for n in sum_:
            sumList.append(int(n))
        ans = tail = ListNode()
        
        for i in sumList[::-1]:
            tail.next = ListNode(i)
            tail = tail.next
        return ans.next