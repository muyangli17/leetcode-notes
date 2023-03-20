import math
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        # adjust Heap
        def adjustHeap(heap: List[tuple], index: int) -> List[tuple]:
            if index >= len(heap) // 2:
                return heap
            if 2 * index + 2 < len(heap):
                if not (heap[index][-1] < heap[2 * index + 1][-1] and heap[index][-1] < heap[2 * index + 2][-1]):
                    if heap[2 * index + 1][-1] < heap[2 * index + 2][-1]:
                        heap[index], heap[2 * index + 1] = heap[2 * index + 1], heap[index]
                        adjustHeap(heap, 2 * index + 1)
                    else:
                        heap[index], heap[2 * index + 2] = heap[2 * index + 2], heap[index]
                        adjustHeap(heap, 2 * index + 2)
            else:
                if heap[index][-1] > heap[2 * index + 1][-1]:
                    heap[index], heap[2 * index + 1] = heap[2 * index + 1], heap[index]
                    adjustHeap(heap, 2 * index + 1)

            return heap

        # build the heap
        def buildHeap(heap: List[tuple]) -> List[tuple]:
            for i in range((len(heap)) // 2 - 1, -1, -1):
                heap = adjustHeap(heap=heap, index=i)

            return heap

        # remove from the heap
        def remove(heap: List[tuple]) -> List[tuple]:
            heap[0], heap[-1] = heap[-1], heap[0]
            heap.pop()
            adjustHeap(heap, 0)
            return heap

        distance = []
        for point in points:
            distance.append((point[0], point[1], math.sqrt(point[0] ** 2 + point[1] ** 2)))

        distance = buildHeap(distance)

        ans = []
        for _ in range(k):
            ans.append([distance[0][0], distance[0][1]])
            distance = remove(distance)

        return ans


points = [[3, 3], [5, -1], [-2, 4]]
k = 2
solution = Solution()
print(solution.kClosest(points=points, k=k))
