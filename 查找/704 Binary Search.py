from typing import List


class Solution:
    def search1(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if target == nums[i]:
                return i
            if target < nums[i]:
                return -1
        return -1

    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if target == nums[m]:
                return m
            if target < nums[m]:
                j = m - 1
            if target > nums[m]:
                i = m + 1
        return -1


solution = Solution()
print(solution.search(nums=[-1, 0, 3, 5, 9, 12], target=2))
