class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        hashT, visit = Counter(nums), set()
        nums.sort()
        res, curr = 1, 0
        for num in nums:
            if num == 1:
                count = hashT[num]
                if count % 2 == 0:
                    count -= 1
                res = max(res, count)
            elif num not in visit and num != 1:
                visit.add(num)
                curr, count = num, 0
                while hashT[curr] >= 2:
                    visit.add(curr)
                    curr *= curr
                    count += 2
                if hashT[curr] == 1:
                    count += 1
                if count % 2 == 0:
                    count -= 1
                res = max(res, count)
                    
        return res