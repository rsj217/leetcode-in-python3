"""
注意 大小写判等

"""
import string


class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = dict()
        for l in string.ascii_letters:
            t[l] = True
        for d in string.digits:
            t[d] = True

        l, r = 0, len(s) - 1
        while l < r:
            if not s[l] in t:
                l += 1
                continue
            if not s[r] in t:
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ("A man, a plan, a canal: Panama", True),
        ]
        self.s = Solution()

    def test_solution(self):
        for s, answer in self.test_case:
            ans = self.s.isPalindrome(s)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
