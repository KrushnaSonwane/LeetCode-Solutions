class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def solve(a, b):
            l, r = 0, len(a) - 1
            while r > l:
                if a[l] != b[r]:
                    t1, t2 = l, r
                    while r > l:
                        if a[l] != a[r]: break
                        l += 1
                        r -= 1
                    else: return True
                    l, r = t1, t2
                    while r > l:
                        if b[l] != b[r]: break
                        l += 1
                        r -= 1
                    else: return True
                    break
                l += 1
                r -= 1
            else: return True
            return False
        return solve(a, b) or solve(b, a) or False