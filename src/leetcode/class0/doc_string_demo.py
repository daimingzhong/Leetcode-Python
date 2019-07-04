"""
arr = [1, 0, 3, 0, 1]  -> list[int],  can also be list.
arr = {1, 0, 3, 0, 1}  -> set[int]

"""

# other docstring:
#
# """reStructuredText docstring (pyCharm Default)
#       :type nums: List
#       :type target: int
#       :rtype: int
#       """
#
# """ numpy docstring
#
# Parameters
# ----------
# nums: int
# target: int
#
# Returns
# -------
#
# """
#
# """ epytext Docstring
#
# @param nums: nums is a shit
# @type nums: int
#
# @param {} target:
# @return:
# """


class TwoSum:
    """
    Given nums = [2, 7, 11, 15], target = 9,
    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
    """
    def two_sum(self, nums, target):
        """Google DocString

        Args:
            nums (list): e.x.  nums = [2, 7, 11, 15]
            target (int):  e.x. target = 9.

        Returns:
            bool:

        """
        return nums


def test():
    ts = TwoSum()
    print(ts.two_sum([2, 7, 11, 15], 9))


if __name__ == "__main__":
    test()
