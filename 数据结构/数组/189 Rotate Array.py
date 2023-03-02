from typing import List


class Solution:
    def rotate1(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        for i in range(k):
            end = nums.pop()
            nums.insert(0, end)

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        double = nums + nums
        for i in range(len(nums)):
            nums[i] = double[len(nums) - k+i]


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3

solution = Solution()
solution.rotate(nums=nums, k=k)
print(nums)
