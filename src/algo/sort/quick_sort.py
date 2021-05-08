import unittest
from src.algo.sort import helper


def partition(nums, lo, hi):
    j = lo
    for i in range(lo, hi):
        if nums[i] <= nums[lo]:
            nums[j], nums[i] = nums[i], nums[j]
            j += 1
    nums[lo], nums[j - 1] = nums[j - 1], nums[lo]
    return j - 1


def quick_sort(nums):
    def _quick_sort(nums, lo, hi):
        if hi - lo <= 1:
            return
        p = partition(nums, lo, hi)
        _quick_sort(nums, lo, p)
        _quick_sort(nums, p + 1, hi)

    _quick_sort(nums, 0, len(nums))


# [lo, l) [l, g], (g, hi)
def quick_3way_sort(nums):
    def dfs(nums, lo, hi):
        if hi - lo <= 1:
            return
        curnum = nums[lo]
        l, i, g = lo, lo, hi - 1
        while i <= g:
            if nums[i] < curnum:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
                i += 1
            elif curnum < nums[i]:
                nums[i], nums[g] = nums[g], nums[i]
                g -= 1
            else:
                i += 1

        dfs(nums, lo, l)
        dfs(nums, g + 1, hi)

    dfs(nums, 0, len(nums))


class TestMain(unittest.TestCase):

    def setUp(self) -> None:
        self.test_case = [
            [],
            [0, 0, 0],
            [10, 3, 1, 1],
            helper.random_nums(100, 0, 100)
        ]

    def test_solution(self):
        for nums in self.test_case:
            # quick_sort(nums)
            quick_3way_sort(nums)
            self.assertTrue(helper.is_sorted(nums))


if __name__ == '__main__':
    unittest.main()
