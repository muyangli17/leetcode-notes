from typing import List


class Solution:
    def generate1(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        else:
            res = [[1], [1, 1]]
            for i in range(2, numRows):
                layer = [1]
                for j in range(len(res[-1]) - 1):
                    layer.append(res[-1][j] + res[-1][j + 1])
                layer.append(1)

                res.append(layer)
            return res

    def generate(self, numRows: int) -> List[List[int]]:
        def combination(n: int, m: int) -> int:
            """
            :param n choosing m:
            :return: number of choosing
            """
            if m < n // 2:
                return combination(n, n - m)
            ans = 1
            for i in range(n, n - m, -1):
                ans *= i
            for i in range(1, m + 1):
                ans //= i
            return ans

        res = [[1]]
        for i in range(1, numRows):
            layer = []
            for j in range(len(res[-1]) + 1):
                layer.append(combination(i, j))

            res.append(layer)
        return res


solution = Solution()
print(solution.generate(5))
