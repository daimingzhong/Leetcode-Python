import sys


"""
{4, 2, -3, 6, 1} is sorted to {-3, 1, 2, 4, 6}
"""


class SelectionSort:
    def solve(self, arr: list) -> list:
        # write your solution here
        for i in range(len(arr) - 1):  # 设置成[), 可能就是为了这里len方便？
            # min = -sys.maxsize - 1
            mini = i  # min 是python关键词，用mini maxi
            for j in range(i, len(arr)):
                if arr[j] < arr[mini]:
                    mini = j
            arr[i], arr[mini] = arr[mini], arr[i]
        return arr


def test():
    tmp = SelectionSort()
    arr = [4, 2, -3, 6, 1]
    tmp.solve(arr)
    print(arr)


if __name__ == '__main__':
    test()