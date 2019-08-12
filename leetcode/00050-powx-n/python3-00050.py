class Solution:
    def myPow(self, x: float, n: int) -> float:
        pow = 1.0
        if n < 0:
            x = 1 / x
            n = -n
        while n > 0:
            if n & 1 == 1:
                pow *= x
            x = x * x
            n //= 2
        return pow