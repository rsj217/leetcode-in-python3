import unittest


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i = len(s) - 1
        j = len(t) - 1
        i_skip = 0
        j_skip = 0
        while 0 <= i or 0 <= j:
            if 0 <= i:
                if s[i] == "#":
                    i_skip += 1
                    i -= 1
                    continue
                if i_skip > 0:
                    i_skip -= 1
                    i -= 1
                    continue

            if 0 <= j:
                if t[j] == "#":
                    j_skip += 1
                    j -= 1
                    continue
                if j_skip > 0:
                    j_skip -= 1
                    j -= 1
                    continue

            if 0 <= i and 0 <= j:
                if s[i] != t[j]:
                    return False
            i -= 1
            j -= 1
        return i == j


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ("ab#c", "ad#c", True),
            ("ab##", "c#d#", True),
            ("a##c", "#a#c", True),
            ("a#c", "b", False),
            ("xywrrmp", "xywrrmu#p", True),
            ("gtc#uz#", "gtcm##uz#", True),
            ("bxj##tw", "bxj###tw", False),
            ("ab##", "c#d#", True),
        ]
        self.s = Solution()

    def test_solution(self):
        for s, t, answer in self.test_case:
            ans = self.s.backspaceCompare(s, t)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
