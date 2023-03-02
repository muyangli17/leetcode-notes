from typing import List


class Solution:
    def moveZeroes1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroNum = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 0:
                zeroNum += 1
                for j in range(i, len(nums) - zeroNum):
                    nums[j] = nums[j + 1]
                nums[-zeroNum] = 0

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nonZero = 0
        for i in range(len(nums)):
            if not nums[i] == 0:
                nums[nonZero] = nums[i]
                nonZero += 1
        for i in range(nonZero, len(nums)):
            nums[i] = 0


nums = [0, 1, 0, 3, 12]

solution = Solution()
solution.moveZeroes(nums=nums)
print(nums)
