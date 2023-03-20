from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # adjust Heap
        def adjustHeap(nums: List[int], index: int) -> List[int]:
            if index >= len(nums) // 2:
                return nums
            if 2 * index + 2 < len(nums):
                if not (nums[index] > nums[2 * index + 1] and nums[index] > nums[2 * index + 2]):
                    if nums[2 * index + 1] > nums[2 * index + 2]:
                        nums[index], nums[2 * index + 1] = nums[2 * index + 1], nums[index]
                        adjustHeap(nums, 2 * index + 1)
                    else:
                        nums[index], nums[2 * index + 2] = nums[2 * index + 2], nums[index]
                        adjustHeap(nums, 2 * index + 2)
            else:
                if nums[index] < nums[2 * index + 1]:
                    nums[index], nums[2 * index + 1] = nums[2 * index + 1], nums[index]
                    adjustHeap(nums, 2 * index + 1)

            return nums

        # build the heap
        def buildHeap(nums: List[int]) -> List[int]:
            for i in range((len(nums)) // 2 - 1, -1, -1):
                nums = adjustHeap(nums=nums, index=i)

            return nums

        # remove from the heap
        def remove(nums: List[int]) -> List[int]:
            nums[0], nums[-1] = nums[-1], nums[0]
            nums.pop()
            adjustHeap(nums, 0)
            return nums

        nums = buildHeap(nums=nums)

        for _ in range(k - 1):
            nums = remove(nums)

        return nums[0]


nums = [3, 2, 1, 5, 6, 4]
k = 2

solution = Solution()
print(solution.findKthLargest(nums=nums, k=k))
