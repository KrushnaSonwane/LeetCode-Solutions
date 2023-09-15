class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        
        def getNum(i):
            res = 0
            while i < len(s) and s[i] not in '+-/*':
                res = res*10+int(s[i])
                i += 1
            return res, i

        num, sign = [], []
        a, i = getNum(0)
        num.append(a)
        while len(s) > i:
            if s[i] == '+':
                sign.append('+')
                a, i = getNum(i+1)
                num.append(a)
            elif s[i] == '-':
                sign.append('-')
                a, i = getNum(i+1)
                num.append(a)
            elif s[i] == '*':
                b, i = getNum(i+1)
                num.append(num.pop() * b)
            else:
                b, i = getNum(i+1)
                num.append(num.pop() // b)
        res = num.pop(0)
        while sign:
            a = sign.pop(0)
            if a == '+':
                res = res + num.pop(0)
            else:
                res = res - num.pop(0)
        return res