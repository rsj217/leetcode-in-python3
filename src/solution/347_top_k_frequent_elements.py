"""
`Problem <https://leetcode-cn.com/problems/top-k-frequent-elements/>`_
-----------------------------------------------------------------------------

347. 前 K 个高频元素

给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。

::

    示例 1:

    输入: nums = [1,1,1,2,2,3], k = 2
    输出: [1,2]
    示例 2:

    输入: nums = [1], k = 1
    输出: [1]

    提示：

    1 <= nums.length <= 105
    k 的取值范围是 [1, 数组中不相同的元素的个数]
    题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的

    进阶：你所设计算法的时间复杂度 必须 优于 O(n log n) ，其中 n是数组大小。



Tips
------

1. 最大堆 heapq
2. heapq 实现是最小堆，对于数字，乘以 -1 变成最大堆

Answer
------

"""
from typing import List
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 统计频次
        dct = {}
        for item in nums:
            dct[item] = dct.get(item, 0) + 1

        # (-1 * 频次，数字) 入堆，乘以了 -1， 最小堆变最大堆
        h = []
        for key, val in dct.items():
            heapq.heappush(h, (-1 * val, key))

        # 出堆
        ans = []
        for _ in range(k):
            _, key = heapq.heappop(h)
            ans.append(key)
        return ans


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([1,1,1,2,2,3], 2, [1, 2]),
            ([1], 1, [1])
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, k, answer in self.test_case:
            ans = self.s.topKFrequent(nums, k)
            self.assertListEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
