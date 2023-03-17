from typing import List


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
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

        def query(target: int) -> int:
            sum = 0
            count = 0
            for number in nums:
                sum += number
                if sum > target:
                    return count
                else:
                    count += 1
            return len(nums)

        qSort(0, len(nums) - 1)

        res = []
        for num in queries:
            res.append(query(num))

        return res


nums = [4, 5, 2, 1]
queries = [3, 10, 21]
solution = Solution()
print(solution.answerQueries(nums=nums, queries=queries))
