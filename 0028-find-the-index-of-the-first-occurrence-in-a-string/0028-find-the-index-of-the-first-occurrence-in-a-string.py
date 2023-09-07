class Solution(object):
    def strStr(self, a, b):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n1, n2 = len(a), len(b)
        j = 0
        if n2 > n1: return -1
        for i in range(n1):
            if a[i] == b[0]:
                ptr1, ptr2 = i, 0
                while n1 > ptr1 and n2 > ptr2 and a[ptr1] == b[ptr2]:
                    ptr1 += 1
                    ptr2 += 1
                if ptr2 == n2: return i
        return -1
                    
                    