class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        stack = []
        for num in nums[::-1]:
            while stack and stack[-1] < num:
                stack.pop()
            if stack:
                stack[-1] += num
            else:
                stack.append(num)
        return stack.pop(0)