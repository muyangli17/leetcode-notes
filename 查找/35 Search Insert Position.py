from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        while i <= j:
            m = i + (j - i) // 2
            if target == nums[m]:
                return m
            if target < nums[m]:
                j = m - 1
            if target > nums[m]:
                i = m + 1
        return i
