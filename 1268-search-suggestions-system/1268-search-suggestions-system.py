class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        A = sorted([word for word in products])
        res = []
        for i, ch in enumerate(searchWord):
            temp = []
            for word in A:
                if len(word) <= i: continue
                if word[i] == ch:
                    temp.append(word)
            res.append(temp[0: min(3, len(temp))])
            A = temp.copy()
        return res