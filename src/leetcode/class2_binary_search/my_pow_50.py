"""
Implement pow(x, n), which calculates x raised to the power n (xn).

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

"""


class MyPow_50:
    def myPow(self, x, n):
        if n == 0:
            return 1.0
        if n == 1:
            return x
        if n == -1:
            return 1/x
        # take care of python 3
        temp = self.myPow(x, n // 2)
        if n % 2 == 0:
            return temp * temp
        else:
            if n > 0:
                return temp * temp * x
            else:
                return temp * temp * 1/x


if __name__ == "__main__":
    my_pow = MyPow_50()
    res = my_pow.myPow(3, 3)
    res = my_pow.myPow(2, 3)
    print(res)
