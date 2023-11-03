class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        for num in range(1, min(target[-1], n) + 1):
            if target and target[0] == num:
                res.append("Push")
                target.pop(0)
            else:
                res.append("Push")
                res.append("Pop")
        return res