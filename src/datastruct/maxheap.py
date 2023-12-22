from typing import List
from dataclasses import dataclass, field
import unittest


@dataclass
class MaxHeap:
    _data: List[int] = field(default_factory=list)
    
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


def print_heap(nums) -> str:
    size = len(nums)
    i = 0
    height = 1
    while 2 * i + 1 < size:
        height += 1
        i = 2 * i + 1
    
    width = (1 << height) - 1
    ans = [[" " for _ in range(width)] for _ in range(height)]
    
    def dfs(seq, deep, lo, hi):
        if seq >= size:
            return
        mid = lo + (hi - lo) // 2
        ans[deep][mid] = str(nums[seq])
        dfs(2 * seq + 1, deep + 1, lo, mid)
        dfs(2 * seq + 2, deep + 1, mid + 1, hi)
    
    dfs(0, 0, 0, width)
    return "\n".join(["".join(line) for line in ans])


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


class TestPrintHeap(unittest.TestCase):
    
    def test_print(self):
        for i in range(10):
            nums = list(range(i))
            print(i, nums)
            s = print_heap(nums)
            print(s)
            print()


if __name__ == '__main__':
    unittest.main()
