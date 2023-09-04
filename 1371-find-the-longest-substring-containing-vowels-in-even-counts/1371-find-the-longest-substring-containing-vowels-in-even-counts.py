class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        hashT, res = {(0,0,0,0,0): -1}, 0
        a, e, i, o, u = 0,0,0,0,0
        for j, ch in enumerate(s):
            if ch == 'a': a += 1
            if ch == 'e': e += 1
            if ch == 'i': i += 1
            if ch == 'o': o += 1
            if ch == 'u': u += 1
            if (a%2, e%2, i%2, o%2, u%2) in hashT:
                res = max(res, j - hashT[(a%2, e%2, i%2, o%2, u%2)])
            else:
                hashT[(a%2, e%2, i%2, o%2, u%2)] = j
        return res