class Solution:
    def minimumLength(self, s: str) -> int:
        l, r = 0, len(s) - 1
        while r > l:
            first = s[l]
            flag = False
            while r >= l and s[r] == first:
                r -= 1
                flag = True
            if flag:
                while r >= l and s[l] == first:
                    l += 1
            else: break
        return r - l + 1