class Solution:
    def containsDuplicate(self, nums) -> bool:
        hash = dict()
        for num in nums:
            if num in hash:
                return True
            hash.update({num: 1})
        return False


solution = Solution()
print(solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
