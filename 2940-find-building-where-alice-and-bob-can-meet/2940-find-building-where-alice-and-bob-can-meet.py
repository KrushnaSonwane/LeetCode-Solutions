class Solution:
    def leftmostBuildingQueries(self, H: List[int], Q: List[List[int]]) -> List[int]:
        i, stack = len(H)-1, []
        for q in Q:
            q.sort()
        Q = [[k[0], k[1], i] for i, k in enumerate(Q)]
        Q.sort(key = lambda x: (-x[1], -x[0]))
        res = [-1 for i in Q]
        for l, r, j in Q:
            if H[r] > H[l] or r == l:
                res[j] = r
            else:
                while r <= i:
                    while stack and stack[-1][0] <= H[i]:
                        stack.pop()
                    stack.append([H[i], i])
                    i -= 1
                p1, p2 = 0, len(stack)-1
                while p2 >= p1:
                    mid = (p2 + p1) // 2
                    if stack[mid][0] <= H[l]:
                        p2 = mid - 1
                    else:
                        res[j] = stack[mid][1]
                        p1 = mid + 1
        return res