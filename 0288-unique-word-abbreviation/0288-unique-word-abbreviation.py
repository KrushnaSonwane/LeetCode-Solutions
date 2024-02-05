class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.A = defaultdict(set)
        for w in dictionary:
            n = w[0] + str(len(w)-2) + w[-1]
            if len(w) <= 2:
                self.A[w].add(w)
            else:
                self.A[n].add(w)

    def isUnique(self, w: str) -> bool:
        n = w[0] + str(len(w)-2) + w[-1]
        if w in self.A[n] and len(self.A[n]) == 1: return True
        if len(self.A[n]) == 0: return True
        return False


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)