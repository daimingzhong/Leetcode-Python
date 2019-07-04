import sys

from typing import List
# arr: List[int]

def max_int():
    max_int_in_python3 = sys.maxsize
    min_int_in_python3 = -sys.maxsize - 1

def swap(arr, fast, slow):
    # 交换两个数, e.x. arr = [1,3,2]
    tmp = arr[fast]
    arr[fast]= arr[slow]
    arr[slow] = tmp

    arr[fast], arr[slow] = arr[slow], arr[fast]