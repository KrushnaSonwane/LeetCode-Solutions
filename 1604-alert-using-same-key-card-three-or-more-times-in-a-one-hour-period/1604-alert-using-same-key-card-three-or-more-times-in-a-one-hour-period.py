class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        res = []
        hashT = defaultdict(list)
        for a, time in zip(keyName, keyTime):
            hashT[a].append([int(time[:2]), int(time[3:])])
        for a in hashT:
            hashT[a].sort()
        for a in hashT:
            for i in range(2, len(hashT[a])):
                m, s = hashT[a][i-2]
                mm, ss = hashT[a][i]
                if m == mm:
                    time = ss - s
                else:
                    time = ((60 * (mm - m - 1))) + (60 - s) + ss
                if time <= 60:
                    res.append(a)
                    break
        return sorted(res)