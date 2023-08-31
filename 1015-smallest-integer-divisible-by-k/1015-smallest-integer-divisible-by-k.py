class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        visit, mod = set(), 1%k
        while mod != 0:
            if mod in visit: return -1
            visit.add(mod)
            mod = (mod*10 + 1) % k
        return len(visit)+1