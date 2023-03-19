import math
from typing import List


class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:
        linearSum = 0
        squaredSum = 0
        N = len(nums) + 2
        for num in nums:
            linearSum += num
            squaredSum += num ** 2

        linearSum = N * (N + 1) // 2 - linearSum
        squaredSum = N * (N + 1) * (2 * N + 1) // 6 - squaredSum

        a = int((linearSum + math.sqrt(2 * squaredSum - linearSum ** 2)) / 2)
        b = linearSum - a

        return [a, b]


nums = [2, 3]
solution = Solution()
print(solution.missingTwo(nums=nums))
