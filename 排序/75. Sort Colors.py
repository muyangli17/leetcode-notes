from typing import List


class Solution:
    def sortColors1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def qSort(left: int, right: int):
            i = left
            j = right

            x = nums[i]

            while i < j:
                while i < j and nums[j] >= x:
                    j -= 1
                while i < j and nums[i] <= x:
                    i += 1

                nums[i], nums[j] = nums[j], nums[i]

            nums[left] = nums[i]
            nums[i] = x

            if j > left:
                qSort(left, i - 1)
            if i < right:
                qSort(j + 1, right)

        qSort(0, len(nums) - 1)

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        count0 = count1 = count2 = 0
        for num in nums:
            if num == 0:
                count0 += 1
            elif num == 1:
                count1 += 1
            else:
                count2 += 1

        for i in range(0, count0, 1):
            nums[i] = 0
        for i in range(count0, count0 + count1, 1):
            nums[i] = 1
        for i in range(count0 + count1, count0 + count1 + count2, 1):
            nums[i] = 2


nums = [2, 0, 2, 1, 1, 0]
solution = Solution()
solution.sortColors(nums)
print(nums)
