from typing import List


class Solution:
    def frequencySort(self, s: str) -> str:

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
        for char in s:
            if char in record:
                record[char] += 1
            else:
                record[char] = 1

        freq = []
        for element in record:
            freq.append((element, record[element]))

        freq = buildHeap(freq)

        ans = ""
        for k in range(len(record)):
            ch = freq[0][0]
            f = freq[0][1]
            ans = ans + ch * f
            freq = remove(freq)

        return ans


s = "Aabb"

solution = Solution()
print(solution.frequencySort(s=s))
