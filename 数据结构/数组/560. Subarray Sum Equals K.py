from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            j = i + 1
            sum = nums[i]
            while j < len(nums) and sum < k:
                sum += nums[j]
                j += 1
            if sum == k:
                count += 1
        return count


solution = Solution()
nums = [1, 2, 3]
k = 3
print(solution.subarraySum(nums, k))
