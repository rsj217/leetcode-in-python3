class Solution:
    def firstUniqChar(self, s: str) -> int:
        t = dict()
        for i in s:
            t[i] = t.get(i, 0) + 1

        for index, item in enumerate(s):
            if t[item] == 1:
                return index
        return -1


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ("leetcode", 0),
            ("loveleetcode", 2),
            ("aabb", -1),
        ]
        self.s = Solution()

    def test_solution(self):
        for s, answer in self.test_case:
            ans = self.s.firstUniqChar(s)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
