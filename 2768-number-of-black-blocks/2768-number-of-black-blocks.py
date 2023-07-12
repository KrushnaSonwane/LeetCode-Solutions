class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        hashT = defaultdict(int)
        for r, c in coordinates:
            t = ''
            for x, y in sorted([[r, c], [r, c - 1], [r + 1, c - 1], [r + 1, c]]):
                if x == m or y == -1: break
                t += str(x)+str(y)
            else:
                hashT[t] += 1
            t = ''
            for x, y in sorted([[r, c], [r, c - 1], [r-1, c-1], [r-1, c]]):
                if -1 in [x, y]: break
                t += str(x)+str(y)
            else:
                hashT[t] += 1
            t = ''
            for x, y in sorted([[r, c], [r-1, c], [r-1, c+1], [r, c + 1]]):
                if x == -1 or y == n: break
                t += str(x)+str(y)
            else:
                hashT[t] += 1
            t = ''
            for x, y in sorted([[r, c], [r+1, c], [r, c+1], [r+1,c+1]]):
                if x == m or y == n: break
                t += str(x)+str(y)
            else:
                hashT[t] += 1
        total = (m-1) * (n-1)
        res = [0] * 5
        res[0] = total - len(hashT)
        for i in range(1, 5):
            count = 0
            for val in hashT.values():
                count += val == i
            res[i] = count
        return res