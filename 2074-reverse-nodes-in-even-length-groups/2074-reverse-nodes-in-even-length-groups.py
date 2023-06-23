# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def rev(p1, p2):
            if p2 > p1:
                arr[p1], arr[p2] = arr[p2], arr[p1]
                rev(p1 + 1, p2 - 1)
        
        arr, temp = [], head
        while temp: 
            arr.append(temp.val)
            temp = temp.next
        currSize, n, i = 1, len(arr), 0
        
        while n >= currSize:
            if not currSize % 2:
                rev(i, i + currSize - 1)
            i += currSize
            n -= currSize
            currSize += 1
            
        if not n % 2: rev(i, len(arr) - 1)
            
        temp = head
        for num in arr:
            temp.val = num
            temp = temp.next
        return head