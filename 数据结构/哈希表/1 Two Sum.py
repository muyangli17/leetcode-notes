from typing import List


class Solution:
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        records = dict()

        for idx, val in enumerate(nums):
            if target - val not in records:
                records[val] = idx
            else:
                return [records[target - val], idx]  # 如果存在就返回字典记录索引和当前索引


nums = [2, 7, 11, 15]
target = 9

solution = Solution()
print(solution.twoSum(nums=nums, target=target))
