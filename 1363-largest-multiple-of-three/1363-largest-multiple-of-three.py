class Solution:
    def largestMultipleOfThree(self, A: List[int]) -> str:
        hashT = Counter(A)
        if A.count(0) == len(A): return '0'
        sum_ = sum(A)
        mod = defaultdict(list)
        for a in A:
            mod[a%3].append(a)
        mod[1].sort(); mod[2].sort()
        if sum_%3==0: 
            pass
        elif sum_ % 3 == 1:
            if len(mod[1]) > 0:
                hashT[mod[1][0]] -= 1
            elif len(mod[2]) > 1:
                hashT[mod[2][0]] -= 1
                hashT[mod[2][1]] -= 1
            else:
                return ''
        else:
            if len(mod[2]) > 0:
                hashT[mod[2][0]] -= 1
            elif len(mod[1]) > 1:
                hashT[mod[1][0]] -= 1
                hashT[mod[1][1]] -= 1
            else:
                return ''
        res = []
        for num in sorted(hashT.keys())[::-1]:
            res.append(str(num)*hashT[num])
        res = ''.join(res)
        if not res: return ''
        if res.count('0') == len(res): return '0'
        return res