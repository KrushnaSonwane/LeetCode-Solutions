class Solution:
    def furthestBuilding(self, H: List[int], bricks: int, ladders: int) -> int:

        def check(k):
            l, b = ladders, bricks
            for num, i in A[::-1]:
                if i <= k:
                    if l:
                        l -= 1
                    elif b >= num:
                        b -= num
                    else: return False
            return True
    
        A = []
        for i in range(1, len(H)):
            if H[i] > H[i-1]:
                A.append([H[i]-H[i-1], i])
        res = 0
        l, r = 1, len(H)-1
        A.sort()
        while r >= l:
            mid = (r + l) // 2
            if check(mid):
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        return res