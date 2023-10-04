class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        A, res = [i for i in range(len(deck))], [0 for _ in deck]
        deck.sort()
        while len(A) > 1:
            i, j = A.pop(0), A.pop(0)
            res[i] = deck.pop(0)
            A.append(j)
        res[A.pop()] = deck.pop()
        return res