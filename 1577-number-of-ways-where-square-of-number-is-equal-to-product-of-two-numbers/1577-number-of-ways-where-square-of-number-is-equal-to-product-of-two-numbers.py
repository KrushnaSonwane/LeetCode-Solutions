class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def solve(nums1, nums2):
            hashT = defaultdict(int)
            for num in nums1:
                hashT[num**2]+=1
            res = 0
            for i in range(len(nums2)):
                for j in range(i+1, len(nums2)):
                    curr = nums2[i]*nums2[j]
                    if curr in hashT: res += hashT[curr]
            return res
        return solve(nums1, nums2) + solve(nums2, nums1)