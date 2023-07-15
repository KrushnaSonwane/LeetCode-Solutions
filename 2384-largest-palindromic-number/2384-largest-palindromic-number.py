class Solution:
    def largestPalindromic(self, num: str) -> str:
        hashT = collections.Counter(num)
        A, B, res = {}, [], []
        for n in hashT:
            if hashT[n]%2 == 0: A[n] = hashT[n]
            elif hashT[n] > 1: A[n] = hashT[n]-1
            if hashT[n] % 2: B.append(n)
        for digit in sorted(A.keys())[::-1]:
            for _ in range(A[digit]//2): res.append(digit)
        if ('0' in res and res.count('0') == len(res)) or not res: return max(B) if B else '0'
        return ''.join(res) + (max(B) if B else '') + ''.join(res[::-1])