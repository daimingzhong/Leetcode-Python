class MergeSort:
    def __init__(self):
        pass

    def merge_sort(self, array):
        # if is not array
        if array is None or len(array) == 0:
            return array
        helper = [0] * len(array)
        self.__merge_helper(array, helper, 0, len(array) - 1)
        return array

    def __merge_helper(self, array, helper, left, right):
        if left >= right:
            return
        mid = (left + right) // 2  # mid = int((right + left) / 2)
        self.__merge_helper(array, helper, left, mid)
        self.__merge_helper(array, helper, mid + 1, right)
        self.__merge(array, helper, left, mid, right)

    def __merge(self, array, helper, left, mid, right):
        # print("left is" + str(left))
        # print(right)
        for i in range(left, right + 1):
            helper[i] = array[i]
        left_index = left
        right_index = mid + 1
        while left_index <= mid and right_index <= right:
            if helper[left_index] <= helper[right_index]:
                array[left] = helper[left_index]
                left += 1
                left_index += 1
            else:
                array[left] = helper[right_index]
                left += 1
                right_index += 1
        while left_index <= mid:
            array[left] = helper[left_index]
            left += 1
            left_index += 1


def main():
    merge_sort = MergeSort()
    array = [1, 4, 2, 3]
    res = merge_sort.merge_sort(array)
    print(res)


if __name__ == "__main__":
    main()
