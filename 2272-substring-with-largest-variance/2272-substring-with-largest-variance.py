class Solution:
    def largestVariance(self, s: str) -> int:
        chr_idxs = defaultdict(lambda: [])
        for i,c in enumerate(s):
            chr_idxs[c].append(i)
        res = 0
        for a,b in itertools.combinations(chr_idxs,2):
            last_a,last_b=-1,-1
            prev_min,prev_max = defaultdict(int),defaultdict(int)
            cur = 0
            idxs = list(sorted(chr_idxs[a]+chr_idxs[b]))
            for ii,i in enumerate(idxs):
                if s[i]==a:
                    last_a=ii
                    cur+=1
                elif s[i]==b:
                    last_b=ii
                    cur-=1
                ii2 = min(last_a,last_b)
                if ii2>=0:
                    res = max(res, cur-prev_min[ii2-1], prev_max[ii2-1]-cur)
                prev_min[ii]=min(prev_min[ii-1],cur)
                prev_max[ii]=max(prev_max[ii-1],cur)
        return res