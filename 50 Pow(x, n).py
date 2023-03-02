class Solution:
    def myPow(self, x: float, n: int) -> float:
        negPow = True
        res = 1
        if n == 0:
            return 1
        if n < 0:
            (negPow, n) = (True, -n)
        while n > 0:
            if n % 2 == 1:
                res *= x
            (x, n) = (x * x, n // 2)
        if negPow:
            res = 1 / res
        return res
