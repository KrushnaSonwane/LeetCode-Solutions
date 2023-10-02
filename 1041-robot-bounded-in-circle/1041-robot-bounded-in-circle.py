class Solution:
    def isRobotBounded(self, S: str) -> bool:
        left = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}
        right = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
        visit, ptr = set({(0,0,0)}), 0
        i, j, D = 0, 0, 'N'
        for _ in range(10**5):
            if S[ptr] == 'L':
                D = left[D]
            elif S[ptr] == 'R':
                D = right[D]
            else:
                if D == 'N':
                    j += 1
                elif D == 'W':
                    i -= 1
                elif D == 'S':
                    j -= 1
                else:
                    i += 1
            ptr = (ptr + 1) % len(S)
            if (i, j, ptr) in visit:
                return True
            visit.add((i, j, ptr))
        return False