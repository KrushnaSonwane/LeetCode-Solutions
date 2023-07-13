class Solution:
    def camelMatch(self, Q: List[str], P: str) -> List[bool]:
        N, res = len(Q), []
        for word in Q:
            i = 0
            for ch in word:
                if ch == ch.upper():
                    if len(P) > i and P[i] == ch: i += 1
                    else: 
                        res.append(False)
                        break
                elif len(P) > i and P[i] == ch: i += 1
            else: res.append(i == len(P))
        return res