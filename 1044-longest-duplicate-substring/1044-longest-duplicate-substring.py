class Solution:
    def longestDupSubstring(self, s: str) -> str:

        def check(size):
            hashT = defaultdict(int)
            for i in range(size, len(s)+1):
                a = s[i-size: i]
                hashT[a] += 1
                if hashT[a] == 2:
                    res[0] = a
                    return True
            return False
            
        l, r = 1, len(s)
        res = ['']

        while r >= l:
            mid = (r+l) // 2
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
            
        return res[0]