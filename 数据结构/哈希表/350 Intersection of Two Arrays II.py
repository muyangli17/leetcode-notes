from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = dict()
        for e in nums1:
            if e in dict1:
                dict1[e] += 1
            else:
                dict1[e] = 1

        dict2 = dict()
        for e in nums2:
            if e in dict2:
                dict2[e] += 1
            else:
                dict2[e] = 1
        res = []
        for key in dict1:
            if key in dict2:
                res = res + [key] * min(dict1[key], dict2[key])
        return res


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

solution = Solution()
print(solution.intersect(nums1=nums1, nums2=nums2))
