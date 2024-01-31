class Solution:
    def dailyTemperatures(self, A: List[int]) -> List[int]:
        res, stack = [0 for _ in A], []
        for i in range(len(A)-1, -1, -1):
            while stack and A[stack[-1]] <= A[i]:
                stack.pop()
            if stack: res[i] = abs(stack[-1] - i)
            stack.append(i)
        return res