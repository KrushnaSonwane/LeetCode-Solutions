class Solution:
    def smallestString(self, s: str) -> str:
        res = [ch for ch in s]
        if s.count('a') == len(s): return s[:-1] + 'z'
        flag = False
        for i in range(len(s)):
            if not flag and res[i] == 'a': continue
            else:
                ptr = i
                while len(s) > ptr and res[ptr] != 'a':
                    res[ptr] = chr(ord(res[ptr]) - 1)
                    ptr += 1
                    flag = True
                    
                break
        return ''.join(res)