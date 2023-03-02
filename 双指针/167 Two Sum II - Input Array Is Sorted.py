from typing import List


class Solution:
    def twoSum1(self, numbers: List[int], target: int) -> List[int]:
        # 疑似超时
        def binarySearch(searchTarget: int, left: int, right: int) -> int:
            while left <= right:
                mid = (left + right) // 2
                if numbers[mid] == searchTarget:
                    return mid
                elif numbers[mid] < searchTarget:
                    left = mid
                else:
                    right = mid
            return -1

        for i in range(len(numbers)):
            result = binarySearch(searchTarget=target - numbers[i], left=i + 1, right=len(numbers))
            if not result == -1:
                return [i + 1, result + 1]

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while i < j:
            sum = numbers[i] + numbers[j]
            if sum == target:
                return [i + 1, j + 1]
            if sum < target:
                i += 1
            else:
                j -= 1
        return None


numbers = [2, 7, 11, 15]
target = 9
solution = Solution()
print(solution.twoSum(numbers=numbers, target=target))
