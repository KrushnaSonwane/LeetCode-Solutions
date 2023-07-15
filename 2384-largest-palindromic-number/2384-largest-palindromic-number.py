class Solution:
    def largestPalindromic(self, num: str) -> str:
        hashT = collections.Counter(num)
        A, B = {}, []
        for n in hashT:
            if hashT[n]%2 == 0: A[n] = hashT[n]
            else:
                if hashT[n] > 1: A[n] = hashT[n]-1
                B.append(n)
        res = []
        for digit in '9876543210':
            if digit in A:
                for _ in range(A[digit]//2): res.append(digit)
        if ('0' in res and res.count('0') == len(res)) or not res:
            return max(B) if B else '0'
        return ''.join(res) + (max(B) if B else '') + ''.join(res[::-1])