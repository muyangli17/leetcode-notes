from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # DP超时
        res = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    res[i] = max(res[i], res[j] + 1)
        # print('result=',res)
        return max(res) >= 3


nums = [2, 1, 5, 0, 4, 6]
solution = Solution()
print(solution.increasingTriplet(nums))
