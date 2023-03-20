from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # adjust Heap
        def adjustHeap(heap: List[tuple], index: int) -> List[tuple]:
            if index >= len(heap) // 2:
                return heap
            if 2 * index + 2 < len(heap):
                if not (heap[index][1] > heap[2 * index + 1][1] and heap[index][1] > heap[2 * index + 2][1]):
                    if heap[2 * index + 1][1] > heap[2 * index + 2][1]:
                        heap[index], heap[2 * index + 1] = heap[2 * index + 1], heap[index]
                        adjustHeap(heap, 2 * index + 1)
                    else:
                        heap[index], heap[2 * index + 2] = heap[2 * index + 2], heap[index]
                        adjustHeap(heap, 2 * index + 2)
            else:
                if heap[index][1] < heap[2 * index + 1][1]:
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

        record = dict()
        for num in nums:
            if num in record:
                record[num] += 1
            else:
                record[num] = 1

        freq = []
        for element in record:
            freq.append((element, record[element]))

        freq = buildHeap(freq)

        ans = []
        for _ in range(k):
            ans.append(freq[0][0])
            freq = remove(freq)

        return ans


nums = [1, 1, 1, 2, 2, 3]
k = 2

solution = Solution()
print(solution.topKFrequent(nums=nums, k=k))
