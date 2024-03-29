from time import time


"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output:  2
Explanation:  There are two ways to climb to the top.

1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output:  3
Explanation:  There are three ways to climb to the top.

1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

1: 1
2: 1+1
3 -> 1+2

"""


def time_record(func):
    def time_func(*args, **kwargs):
        print("============================================================================")
        start = time()
        result_func = func(*args, **kwargs)
        end = time()
        print(func.__name__, 'took', ("%.2f" % (end - start)), "'s time")
        return result_func
    return time_func


class ClimbStairs:
    @time_record
    def climb_stairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        res = [0] * (n + 1)
        res[1], res[2] = 1, 2
        i = 0
        for i in range(3, n + 1):
            res[i] = res[i - 1] + res[i - 2]
        return res[i]

    @staticmethod
    def climb_stairs2(self, n):
        if n == 1:
            return 1
        res = [0 for i in range(n)]
        res[0], res[1] = 1, 2
        for i in range(2, n):
            res[i] = res[i - 1] + res[i - 2]
        return res[-1]


if __name__ == "__main__":
    sol = ClimbStairs()
    print(sol.climb_stairs(500))
