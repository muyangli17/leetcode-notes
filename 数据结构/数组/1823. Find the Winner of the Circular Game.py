class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def leftPlayer(left: list, startIndex: int, k: int) -> int:
            if len(left) == 1:
                return left[0]

            popIndex = (startIndex + k - 1) % len(left)
            left.pop(popIndex)

            return leftPlayer(left=left, startIndex=popIndex, k=k)

        return leftPlayer([_ for _ in range(1, n + 1, 1)], 0, k)


n = 6
k = 5
solution = Solution()
print(solution.findTheWinner(n=n, k=k))
