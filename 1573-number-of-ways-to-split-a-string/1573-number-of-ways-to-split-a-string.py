class Solution:
    def numWays(self, s: str) -> int:
        count = s.count("1")
        res, MOD = 0, 10 ** 9 + 7
        l, r = 0, 0
        ptr, n = 0, len(s)
        if count % 3: return 0
        if count == 0: return (((n - 2) * ((n - 2) + 1)) // 2) % MOD
        count //= 3
        curr = 0
        while curr <= count:
            curr += s[ptr] == '1'
            if curr == count:
                l += 1
            ptr += 1
        curr = 0; ptr = n - 1
        while curr <= count:
            curr += s[ptr] == '1'
            r += curr == count
            ptr -= 1
        return (l * r) % MOD