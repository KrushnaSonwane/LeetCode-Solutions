class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:

        def merge(visit):
            return ''.join(ch for i, ch in enumerate(s) if i not in visit)

        def delAB(s):
            res, stack, visit = 0, [], set()
            for i, ch in enumerate(s):
                if ch == 'a': stack.append(i)
                elif ch == 'b' and stack:
                    visit.add(stack.pop())
                    res += x
                    visit.add(i)
                else: stack = []
            return res, merge(visit)

        def delBA(s):
            res, stack, visit = 0, [], set()
            for i, ch in enumerate(s):
                if ch == 'b': stack.append(i)
                elif ch == 'a' and stack:
                    visit.add(stack.pop())
                    res += y
                    visit.add(i)
                else: stack = []
            return res, merge(visit)

        a, ss = delAB(s)
        b, _ = delBA(ss)
        xx, z = delBA(s)
        yy, _ = delAB(z)
        
        return max(a+b, xx+yy)