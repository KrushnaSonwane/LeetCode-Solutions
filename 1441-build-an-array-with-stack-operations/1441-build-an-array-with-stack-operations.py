class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        def operation():
            res.append("Push")
            res.append("Pop")
        res, i = [], 0
        for num in range(1, min(target[-1], n) + 1):
            if i < len(target):
                if target[i] == num:
                    res.append("Push")
                    i += 1
                else:
                    operation()
            else:
                operation()
        return res