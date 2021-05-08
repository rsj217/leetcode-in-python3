from typing import List
import unittest
from src.algo.sort import helper


def _heap_sort(nums: [List], lo: int, hi: int):
    heapify(nums, lo, hi)
    for i in range(hi - 2, lo, -1):
        nums[lo], nums[i] = nums[i], nums[lo]
        shiftdown(nums, lo, i, lo)


def heapify(nums: List[int], lo: int, hi: int):
    for i in range((hi - 2) // 2, lo - 1, -1):
        shiftdown(nums, lo, hi, i)


def shiftdown(nums: List[int], lo: int, hi: int, k: int):
    while 2 * k + 1 < hi:
        j = 2 * k + 1
        if j + 1 < hi and nums[j] < nums[j + 1]:
            j += 1
        if nums[j] <= nums[k]:
            break
        nums[j], nums[k] = nums[k], nums[j]
        k = j


def heap_sort(nums: List[int]):
    _heap_sort(nums, 0, len(nums))


class TestMain(unittest.TestCase):

    def setUp(self) -> None:
        self.test_case = [
            [],
            [0, 0, 0],
            [0, 3, 1, 1],
            helper.random_nums(100, 0, 100)
        ]

    def test_solution(self):
        for nums in self.test_case:
            heap_sort(nums)


if __name__ == '__main__':
    unittest.main()
