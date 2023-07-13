class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = [str(num) for num in range(1, n + 1)]
        res.sort()
        return [int(num) for num in res]