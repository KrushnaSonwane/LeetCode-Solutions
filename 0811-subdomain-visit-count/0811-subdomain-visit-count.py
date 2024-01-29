class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        A, hashT = [], Counter()
        for name in cpdomains:
            count, domain = name.split()
            i = len(domain)-1
            while i >= 0:
                while i >= 0 and domain[i] != '.':
                    i -= 1
                hashT[domain[i+1:]] += int(count)
                i -= 1
        return [str(hashT[count])+' '+count for count in hashT]