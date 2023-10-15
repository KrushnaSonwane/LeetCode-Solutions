class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        res = []
        stack = []
        count = 0
        for num in words:
            if num == 'prev':
                count += 1
                if len(stack) >= count:
                    res.append(int(stack[-count]))
                else:
                    res.append(-1)
            else:
                count = 0
                stack.append(num)
        return res