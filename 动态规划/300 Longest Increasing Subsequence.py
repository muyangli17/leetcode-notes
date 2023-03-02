from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        F = [1] * len(nums)
        for i in range(1, len(nums)):
            maxval = -1
            for j in range(i):
                if nums[i] > nums[j] and maxval < F[j]:
                    maxval = F[j]
            F[i] = max(F[i], maxval + 1)

        return max(F)


solution = Solution()
print(solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
