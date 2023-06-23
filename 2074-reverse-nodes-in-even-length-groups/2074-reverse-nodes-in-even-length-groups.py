# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr, temp = [], head
        while temp: 
            arr.append(temp.val)
            temp = temp.next
        currSize, n = 1, len(arr)
        i = 0
        while n >= currSize:
            if currSize % 2:
                i += currSize
            else:
                ptr1, ptr2 = i, i + currSize - 1
                while ptr2 > ptr1:
                    arr[ptr2], arr[ptr1] = arr[ptr1], arr[ptr2]
                    ptr1 += 1
                    ptr2 -= 1
                i += currSize
            n -= currSize
            currSize += 1
        if not n % 2:
            ptr1, ptr2 = i, len(arr) - 1
            while ptr2 > ptr1:
                arr[ptr2], arr[ptr1] = arr[ptr1], arr[ptr2]
                ptr1 += 1
                ptr2 -= 1
        temp = head
        for num in arr:
            temp.val = num
            temp = temp.next
        return head