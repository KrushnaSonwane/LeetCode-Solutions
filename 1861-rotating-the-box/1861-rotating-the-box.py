class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        for i in range(m):
            ptr = n - 1
            for j in range(n - 1, -1, -1):
                if box[i][j] == '*': ptr = j - 1
                elif box[i][j] == '#':
                    box[i][j] = '.'
                    box[i][ptr] = '#'
                    ptr -= 1
        return [[box[j][i] for j in range(m)][::-1] for i in range(n)]