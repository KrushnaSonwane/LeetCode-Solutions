class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        AA, BB = [], []
        for num in A:
            if num%2: BB.append(num)
            else: AA.append(num)
        return AA+BB