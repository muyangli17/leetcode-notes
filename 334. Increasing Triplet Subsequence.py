from typing import List


class Solution:
    def increasingTriplet1(self, nums: List[int]) -> bool:
        # DP超时
        res = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    res[i] = max(res[i], res[j] + 1)
        # print('result=',res)
        return max(res) >= 3

    def increasingTriplet(self, nums: List[int]) -> bool:
        INF = pow(2, 31)
        triple = [INF] * 3
        len = 0

        def searchInsert(target: int) -> int:
            i = 0
            j = 2
            while i <= j:
                m = i + (j - i) // 2
                if target == triple[m]:
                    return m
                if target < triple[m]:
                    j = m - 1
                if target > triple[m]:
                    i = m + 1
            return i

        for num in nums:
            insertPos = searchInsert(num)
            triple[insertPos] = num
            len = max(len, insertPos + 1)
            if len == 3:
                return True
        return False


nums = [2, 1, 5, 0, 4, 6]
solution = Solution()
print(solution.increasingTriplet(nums))
