from typing import List
import unittest


class MaxHeap:
    def __init__(self):
        self._data = []

    @property
    def size(self) -> int:
        return len(self._data)

    def heapify(self, nums: List[int]):
        heapify(nums)
        self._data = nums

    def push(self, item: int):
        self._data.append(item)
        shiftup(self._data, self.size - 1)

    def pop(self) -> int:
        assert self.size > 0, "error"
        self._data[0], self._data[self.size - 1] = self._data[self.size - 1], self._data[0]
        item = self._data.pop()
        shiftdown(self._data, 0)
        return item


def heapify(nums: List[int]):
    k = len(nums)
    for i in range((k - 2) // 2, -1, -1):
        shiftdown(nums, i)


def shiftup(nums: List[int], k: int):
    while 0 < k and nums[(k - 1) // 2] < nums[k]:
        nums[(k - 1) // 2], nums[k] = nums[k], nums[(k - 1) // 2]
        k = (k - 1) // 2


def shiftdown(nums: List[int], k: int):
    while 2 * k + 1 < len(nums):
        j = 2 * k + 1
        if j + 1 < len(nums) and nums[j] < nums[j + 1]:
            j = j + 1
        if nums[j] <= nums[k]:
            break
        nums[k], nums[j] = nums[j], nums[k]
        k = j


def print_heap(nums):
    n = len(nums)
    count = len(nums)
    max_level = 0
    number_per_level = 1
    while n > 0:
        max_level += 1
        n -= number_per_level
        number_per_level *= 2

    max_level_number = 2 ** (max_level - 1)
    cur_tree_max_level_number = max_level_number
    index = 1

    for level in range(0, max_level):
        line1 = " " * (max_level_number * 3 - 1)
        cur_level_number = min(count - 2 ** level + 1, 2 ** level)
        is_left = True
        index_cur_level = 0

        while index_cur_level < cur_level_number:
            line1 = put_number_in_line(nums[index - 1], line1, index_cur_level, cur_tree_max_level_number * 3 - 1,
                                       is_left)
            is_left = not is_left
            index += 1
            index_cur_level += 1
        print(line1)

        if level == max_level - 1:
            break

        line2 = " " * (max_level_number * 3 - 1)
        for index_cur_level in range(0, cur_level_number):
            line2 = put_branch_in_line(line2, index_cur_level, cur_tree_max_level_number * 3 - 1)
        print(line2)

        cur_tree_max_level_number //= 2


def put_number_in_line(num, line, index_cur_level, cur_tree_width, is_left):
    sub_tree_width = (cur_tree_width - 1) // 2
    offset = index_cur_level * (cur_tree_width + 1) + sub_tree_width
    if num >= 10:
        line = line[0: offset + 0] + str(num) + line[offset + 2:]
    else:
        if is_left:
            line = line[0:offset + 0] + str(num) + line[offset + 1:]
        else:
            line = line[0: offset + 1] + str(num) + line[offset + 2:]
    return line


def put_branch_in_line(line, index_cur_level, cur_tree_width):
    sub_tree_width = (cur_tree_width - 1) // 2
    sub_sub_tree_width = (sub_tree_width - 1) // 2
    offset_left = index_cur_level * (cur_tree_width + 1) + sub_sub_tree_width
    offset_right = index_cur_level * (cur_tree_width + 1) + sub_tree_width + 1 + sub_sub_tree_width

    line = line[0:offset_left + 1] + "/" + line[offset_left + 2:]
    line = line[0:offset_right] + "\\" + line[offset_right + 1:]

    return line


class TestMaxHeap(unittest.TestCase):

    def test_heapify(self):
        from src.algo.sort import helper
        test_case = (
            [],
            [0, 0, 0],
            [0, 3, 1, 1],
            helper.random_nums(100, 0, 100)
        )

        for nums in test_case:
            heapify(nums)
            self.assertTrue(helper.is_maxheap(nums))


if __name__ == '__main__':
    unittest.main()
