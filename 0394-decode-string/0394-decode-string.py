class Solution:
    def decodeString(self, s: str) -> str:
        stack, num, res = [], 0, ''
        for ch in s:
            if ch == '[':
                stack.append(res)
                stack.append(num)
                res, num = '', 0
            elif ch == ']':
                a, b = stack.pop(), stack.pop()
                res = b + res * a
            elif ch.isdigit():
                num = num * 10 + int(ch)
            else:
                res += ch
        return res