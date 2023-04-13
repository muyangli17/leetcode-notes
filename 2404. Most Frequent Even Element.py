from typing import List


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        record = dict()
        for num in nums:
            if num % 2 == 0:
                if num in record:
                    record[num] += 1
                else:
                    record[num] = 1

        maxCount = 0
        maxNum = -1
        for num in record:
            if record[num] > maxCount:
                maxNum = num
                maxCount = record[num]
            if record[num] == maxCount and num < maxNum:
                maxNum = num
        return maxNum
