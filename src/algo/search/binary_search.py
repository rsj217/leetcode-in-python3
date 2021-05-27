from typing import List


def binary_search(nums: List[int], target: int) -> int:
    return _binary_search(nums, 0, len(nums), target)


def binary_search_min_insert(nums: List, target: int) -> int:
    pass


def _binary_search(nums: List[int], lo: int, hi: int, target: int) -> int:
    while lo < hi:
        mid = lo + (hi - lo) / 2
        if target < nums[mid]:
            hi = mid
        elif nums[mid] < target:
            lo = mid + 1
        else:  # target == nums[mid]
            return mid
    return -1
