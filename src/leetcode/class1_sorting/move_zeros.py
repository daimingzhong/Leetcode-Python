from typing import List

"""
Given an arr of integers, move all the 0s to the right end of the arr.

The relative order of the elements in the original arr does not need to be maintained.

{1, 0, 3, 0, 1} --> {1, 3, 1, 0, 0} or {1, 1, 3, 0, 0} or {3, 1, 1, 0, 0}

        0, 1, 0, 3, 0, 1

fast    0  0  0  3
slow    1 ->
第一次都是0，fast + 1，slow不变。
第二次，互换之后都 + 1

        1, 0, 3,
fast    1
slow    1
第一次都是1，swap之后都+1，

方法1：
快慢指针，对调两个位置的数。
快的指针遇到0，和慢的对调，遇到1向前。
慢的指针指向0。

"""


class MoveZeros:

    def move_zero(self, arr: List[int]) -> list:
        fast, slow = 0, 0
        while fast < len(arr):
            if arr[fast] == 0:
                fast += 1
            else:
                arr[fast], arr[slow] = arr[slow], arr[fast]
                fast += 1
                slow += 1
        return arr


def test():
    mz = MoveZeros()
    arr = [1, 0, 3, 0, 1]
    mz.move_zero(arr)
    print(arr)


if __name__ == "__main__":
    test()
