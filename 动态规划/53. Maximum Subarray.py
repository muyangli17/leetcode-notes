from typing import List


class Solution:
    def maxSubArray1(self, nums: List[int]) -> int:
        # 此解法超时
        neg_INF: int = -999999
        start = 0
        end = 1
        for firstN in range(1, len(nums)):
            original_sum = sum(nums[start: end])
            long_sum = sum(nums[start: firstN + 1])

            max_sum = neg_INF
            max_index = -1
            for index in range(end, firstN + 1):
                potential_sum = sum(nums[index:firstN + 1])
                if potential_sum > max_sum:
                    (max_sum, max_index) = (potential_sum, index)

            potential_direction = [original_sum, long_sum, max_sum]
            key = potential_direction.index(max(potential_direction))

            if key == 0:
                pass
            elif key == 1:
                (start, end) = (start, firstN + 1)
            elif key == 2:
                (start, end) = (max_index, firstN + 1)

        return sum(nums[start:end])

    def maxSubArray2(self, nums: List[int]) -> int:
        # 定义solution[n]为“nums[:n]中最大子序列的和”
        solution = [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            solution[i] = nums[i] + max(solution[i - 1], 0)
        return max(solution)

    def maxSubArray(self, nums: List[int]) -> int:
        # 定义solution[n]为“nums[:n]中最大子序列的和”
        solution = sum = nums[0]
        for i in range(1, len(nums)):
            if sum < 0:
                sum = nums[i]
            else:
                sum += nums[i]
            solution = max(solution, sum)
        return solution


nums = [-83, 20, 49, -64, 94, 18, 11, 48, 16, 2, -26, 47, 99, -21, -50, 55, -23, -94, -73, 46, -85]
solution = Solution()
print(solution.maxSubArray(nums=nums))
