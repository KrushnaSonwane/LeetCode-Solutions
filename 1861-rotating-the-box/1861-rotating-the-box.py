class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        for i in range(m):
            ptr1, ptr2 = n - 1, n - 1
            while ptr1 >= 0:
                if box[i][ptr1] == '*':
                    ptr2 = ptr1 - 1
                if box[i][ptr1] == '#':
                    box[i][ptr1] = '.'
                    box[i][ptr2] = '#'
                    ptr2 -= 1
                ptr1 -= 1
        res = []
        for i in range(n):
            temp = []
            for j in range(m):
                temp.append(box[j][i])
            res.append(temp[::-1])
        return res