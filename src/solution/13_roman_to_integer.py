from typing import List
import unittest


class Solution:
    def romanToInt(self, s: str) -> int:
        t = dict(
            I=1,
            V=5,
            X=10,
            L=50,
            C=100,
            D=500,
            M=1000,
        )
        i = 0
        ans = 0
        while i < len(s):
            if i + 1 < len(s) and  t[s[i]] <  t[s[i+1]]:
                ans += t[s[i+1]] - t[s[i]]
                i += 2
            else:
                ans += t[s[i]]
                i += 1
        return ans

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case= [
            ("MCDLXXVI", 1476),
            ("LVIII", 58),
            ("MCMXCIV", 1994)


        ]
        self.s = Solution()

    def test_solution(self):
        for s, answer in self.test_case:
            ans = self.s.romanToInt(s)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
