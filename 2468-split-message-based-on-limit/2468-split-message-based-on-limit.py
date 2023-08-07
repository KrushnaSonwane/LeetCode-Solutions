class Solution:
    def splitMessage(self, M: str, L: int) -> List[str]:
        def check(size):
            count = 0
            for i in range(1, size+1):
                count += len(str(size)) + len(str(i)) + 3
            total = size*L
            total -= count
            return len(M) <= total
        l, r = 0, 10
        res = inf
        while r >= l:
            mid = (r+l)//2
            if check(mid):
                res = min(res,mid)
                r = mid - 1
            else:
                l = mid + 1
        if res == inf:
            l, r = 10, 100
            while r >= l:
                mid = (r+l)//2
                if check(mid):
                    res = min(res,mid)
                    r = mid - 1
                else:
                    l = mid + 1
        if res == inf:
            l, r = 100, 1000
            while r >= l:
                mid = (r+l)//2
                if check(mid):
                    res = min(res,mid)
                    r = mid - 1
                else:
                    l = mid + 1
        if res == inf:
            l, r = 1000, 10000
            while r >= l:
                mid = (r+l)//2
                if check(mid):
                    res = min(res,mid)
                    r = mid - 1
                else:
                    l = mid + 1
        if res == inf: return []
        ans = []
        j = 0
        for i in range(1, res+1):
            t = []
            for _ in range(L-(len(str(i))+len(str(res))+3)):
                if len(M)>j:
                    t.append(M[j])
                    j += 1
            ans.append(''.join(t) + '<'+str(i)+'/'+str(res)+'>')
        return ans