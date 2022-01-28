import unittest


class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        dp = [0, 1]
        for i in range(2, n + 1):
            dpn = dp[0] + dp[1]
            dp[0], dp[1] = dp[1], dpn
        return dp[1]


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            (0, 0),
            (1, 1),
            (2, 1),
            (3, 2),
            (4, 3),
            (5, 5),
            (6, 8),
            (10, 55),
        ]
        self.s = Solution()

    def test_solution(self):
        for num, answer in self.test_case:
            ans = self.s.fib(num)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
