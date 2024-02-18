class Solution:
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        D = {'r': 'd', 'd': 'l', 'l': 'u', 'u': 'r'}
        step = {'r': [0, 1], 'd': [1, 0], 'l': [0, -1], 'u': [-1, 0]}
        visit = set({(0, 0)})
        count = Counter()
        Q = [(0, 0, 'r')]
        while Q:
            i, j, d = Q.pop(0)
            x, y = step[d]
            i += x; j += y
            if 0 <= i < len(room) and 0 <= j < len(room[0]) and room[i][j] == 0:
                Q.append((i, j, d))
                visit.add((i, j))
            else:
                i -= x
                j -= y
                if count[(i, j)] < 4:
                    Q.append((i, j, D[d]))
                    count[(i, j)] += 1
        return len(visit)