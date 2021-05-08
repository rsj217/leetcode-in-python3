from typing import List
import random


def is_sorted(nums: List[int]) -> bool:
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True


def random_nums(size, l, r) -> List[int]:
    return [random.randint(l, r) for i in range(size)]


def is_maxheap(nums: List[int]) -> bool:
    size = len(nums)
    for index, item in enumerate(nums):
        j = 2 * index + 1
        if j < size and item < nums[j]:
            return False
        if j + 1 < size and item < nums[j + 1]:
            return False
    return True
