class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k%2 == 0: return -1
        visit, mod = set(), 1%k
        while mod != 0:
            if mod in visit: return -1
            visit.add(mod)
            mod = (mod*10) + 1
            mod %= k
        return len(visit)+1