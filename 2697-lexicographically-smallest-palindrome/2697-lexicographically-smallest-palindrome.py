class Solution(object):
    def makeSmallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr = [ch for ch in s]
        l, r = 0, len(arr) - 1
        while r > l:
            if arr[l] > arr[r]:
                arr[l] = arr[r]
            else:
                arr[r] = arr[l]
            l += 1
            r -= 1
        return ''.join(arr)