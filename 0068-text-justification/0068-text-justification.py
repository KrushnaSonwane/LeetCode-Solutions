class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans, t, curr = [], [], 0
        for word in words:
            curr += len(word)
            t.append(word)
            if maxWidth >= len(t)-1+curr:
                continue
            t.pop()
            ans.append(t)
            t = [word]
            curr = len(word)
        if t: ans.append(t)
        res = []
        for i in range(len(ans)-1):
            A = ans[i]
            if len(A)==1: 
                res.append(A[0] + (' ' * (maxWidth-len(A[0]))))
                continue
            currSize = maxWidth
            size = 0
            t = []
            for w in A:
                size += len(w)
            currSize -= size
            space = currSize // (len(A)-1)
            extra = currSize - space * (len(A)-1)
            for w in A:
                if len(t)==0:
                    t.append(w)
                else:
                    t.append(' '*space + (' ' if extra >= 1 else '') + w)
                    extra -= 1
            res.append(''.join(t))
        res.append(' '.join(ans[-1]))
        res[-1] += ' ' * (maxWidth - len(res[-1]))
        return res