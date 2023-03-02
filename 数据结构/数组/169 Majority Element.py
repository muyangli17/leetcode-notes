from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        element = None
        for e in nums:
            if count == 0:
                element = e
                count += 1
            else:
                if element == e:
                    count += 1
                else:
                    count -= 1
        return element
