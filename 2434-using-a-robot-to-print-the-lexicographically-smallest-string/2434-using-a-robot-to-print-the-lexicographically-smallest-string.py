class Solution:
    def robotWithString(self, s: str) -> str:
        hashT, stack, res = Counter(s), [], []
        allCh, ptr = 'abcdefghijklmnopqrstuvwxyz', 0
        for ch in allCh:
            while stack and stack[-1]<=ch:
                res.append(stack.pop())
            if ch in hashT:
                while ch in hashT:
                    if s[ptr]==ch: res.append(s[ptr])
                    else: stack.append(s[ptr])
                    hashT[s[ptr]] -= 1
                    if hashT[s[ptr]] == 0:
                        del hashT[s[ptr]]
                    ptr += 1
        while stack:
            res.append(stack.pop())
        return ''.join(res)