from typing import List
import unittest

"""
贪心：最大的饼干，给最大的孩子
"""
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)
        ans = 0
        gi, si = 0, 0
        while gi < len(g) and si < len(s):
            if g[gi] <= s[si]:
                ans += 1
                si += 1
            gi += 1
        return ans


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([1, 2, 3], [1, 1], 1),
            ([1, 2], [1, 2, 3], 2),
            ([2], [1, 1], 0)
        ]
        self.s = Solution()

    def test_solution(self):
        for g, s, answer in self.test_case:
            ans = self.s.findContentChildren(g, s)
            self.assertEqual(ans, answer)


if __name__ == '__main__':
    unittest.main()
