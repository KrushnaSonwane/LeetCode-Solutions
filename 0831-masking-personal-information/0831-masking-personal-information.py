class Solution:
    def maskPII(self, s: str) -> str:
        res = ''
        if "@" in s:
            res += s[0].lower() + '*****'
            ptr1 = 1
            while s[ptr1] != '@':
                ptr1 += 1
            res += s[ptr1 - 1].lower() + '@'
            ptr1 += 1
            while len(s) > ptr1: 
                res += s[ptr1].lower()
                ptr1 += 1
        else:
            number = []
            for ch in s:
                if ch.isdigit(): number.append(ch)
            n = len(number)
            if n == 10:
                res += "***-***-"
            elif n == 11:
                res += "+*-***-***-"
            elif n == 12:
                res += "+**-***-***-"
            else: res += "+***-***-***-"
            res += ''.join(number[-4:])
        return res