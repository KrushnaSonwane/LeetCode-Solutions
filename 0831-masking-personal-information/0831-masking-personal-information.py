class Solution:
    def maskPII(self, s: str) -> str:
        res = ''
        if "@" in s:
            res += s[0].lower()
            i = s.index("@")
            res += '*****' + s[i - 1].lower() + s[i]
            res += ''.join(ch.lower() for ch in s[i + 1: ])
        else:
            number = []
            for ch in s:
                if ch.isdigit(): number.append(ch)
            n = len(number)
            if n == 10: res += "***-***-"
            elif n == 11: res += "+*-***-***-"
            elif n == 12: res += "+**-***-***-"
            else: res += "+***-***-***-"
            res += ''.join(number[-4:])
        return res