class Solution:
    def minimumLength(self, s: str) -> int:
        res = [ch for ch in s]
        while len(res) > 1:
            first = res[0]
            if len(res) > 1:
                flag = True
                while res and res[-1] == first:
                    res.pop()
                    flag = False
                if not flag:
                    while res and res[0] == first:
                        res.pop(0)
                else:
                    break
            else:
                break
        return len(res)