from typing import List


class Solution:
    def subarraySum1(self, nums: List[int], k: int) -> int:
        # O(n^2) 超时
        count = 0
        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums), 1):
                sum += nums[j]
                if sum == k:
                    count += 1
        return count

    def subarraySum2(self, nums: List[int], k: int) -> int:
        s = 0
        prefixSum = []
        positions = {}
        count = 0
        for index in range(len(nums)):
            s += nums[index]
            prefixSum.append(s)
            if s in positions:
                positions[s].append(index)
            else:
                positions[s] = [index]

        for number in prefixSum:
            if number == k:
                count += 1

        for index in range(len(nums)):
            positions[prefixSum[index]].remove(index)
            if prefixSum[index] + k in positions:
                count += len(positions[prefixSum[index] + k])

        return count

    def subarraySum(self, nums: List[int], k: int) -> int:
        s = 0
        record = {0: 1}
        count = 0
        for index in range(len(nums)):
            s += nums[index]

            if s - k in record:
                count += record[s - k]

            if s in record:
                record[s] += 1
            else:
                record[s] = 1

        return count


solution = Solution()
nums = [1, 1, 1]
k = 2
print(solution.subarraySum(nums, k))
