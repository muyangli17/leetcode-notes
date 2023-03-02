from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        res = []

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                res.append(pow(nums[left], 2))
                left += 1
            else:
                res.append(pow(nums[right], 2))
                right -= 1
        res.reverse()
        return res


solution = Solution()
print(solution.sortedSquares([-5, -3, -2, -1]))
