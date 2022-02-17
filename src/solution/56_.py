"""
`Problem <https://leetcode-cn.com/problems/>`_
-----------------------------------------------------------------------------

以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返
回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。

::

    示例 1：

    输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
    输出：[[1,6],[8,10],[15,18]]
    解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

    示例 2：

    输入：intervals = [[1,4],[4,5]]
    输出：[[1,5]]
    解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。


    提示：

    1 <= intervals.length <= 10⁴
    intervals[i].length == 2
    0 <= starti <= endi <= 10⁴

Tips
------

1. 区间先排序
2. 合并区间，前[i, j] 和 后 [x, y] 的关系，合并这两个区间，更新为新的区间

Answer
------

"""
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        s, e = intervals[0]
        for item in intervals:
            if item[0] <= e:
                e = max(e, item[1])
            else:
                ans.append([s, e])
                s, e = item
        ans.append([s, e])
        return ans



import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [

        ]
        self.s = Solution()

    def test_solution(self):
        pass


if __name__ == '__main__':
    unittest.main()
