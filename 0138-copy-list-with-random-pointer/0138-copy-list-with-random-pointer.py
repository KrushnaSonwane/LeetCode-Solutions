"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashT, temp = {}, head
        ans = tail = Node(-1)
        while temp:
            tail.next = Node(temp.val)
            hashT[temp] = tail.next
            tail = tail.next
            temp = temp.next
        ans = ans.next
        a, b = ans, head
        while b:
            curr = b.random
            if curr:
                a.random = hashT[curr]
            a = a.next
            b = b.next
        return ans