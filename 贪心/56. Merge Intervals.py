from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        # print(intervals)

        merged = []
        k = 0
        l = intervals[0][0]
        r = intervals[0][1]
        while k < len(intervals):
            if intervals[k][0] <= r:
                r = max(intervals[k][1], r)
            else:
                merged.append([l, r])
                l = intervals[k][0]
                r = intervals[k][1]
            k += 1
        merged.append([l, r])
        return merged


intervals = [[1, 3], [8, 10], [2, 6], [15, 18]]
solution = Solution()
print(solution.merge(intervals=intervals))
