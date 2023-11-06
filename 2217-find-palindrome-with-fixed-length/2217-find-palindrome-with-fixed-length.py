class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        total, res = 9, [-1 for i in queries]
        temp = intLength
        while intLength - 2 > 0:
            total *= 10
            intLength -= 2
        for i, q in enumerate(queries):
            if q <= total:
                curr = str(q - 1) 
                num = ['0' for _ in range(temp)]
                num[0], num[-1] = '1', '1'
                l, r = temp // 2 if temp%2 else temp // 2 - 1, temp // 2
                for ch in curr[::-1]:
                    num[l] = num[r] = ch
                    l -= 1
                    r += 1
                if l == -1:
                    num[-1] = num[0] = str(int(curr[0]) + 1)
                res[i] = (int(''.join(num)))
        return res