from typing import List


class Solution:
    def productExceptSelf1(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)

        # 从左右二分别开始计算left 和 right
        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i - 1]
            right[-(i + 1)] = right[-i] * nums[-i]

        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = left[i] * right[i]
        return res

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = right = 1
        res = [1] * len(nums)

        # 两次遍历分别计算每个点对应的left和right
        for i in range(1, len(nums)):
            left = left * nums[i - 1]
            res[i] = left

        for i in range(-2, -len(nums)-1, -1):
            right = right * nums[i + 1]
            res[i] *= right
        return res


nums = [1, 2, 3, 4]
solution = Solution()
print(solution.productExceptSelf(nums=nums))
