import unittest


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        d = dict()
        for idx in range(len(s)):
            d[s[idx]] = d.get(s[idx], 0) + 1
            d[t[idx]] = d.get(t[idx], 0) - 1
        
        for _, v in d.items():
            if v != 0:
                return False
        return True


class TestSolution(unittest.TestCase):
    
    def setUp(self):
        self.test_case = [
            ("anagram", "nagaram", True),
            ("rat", "car", False),
        ]
        self.s = Solution()
    
    def test_solution(self):
        for s, t, answer in self.test_case:
            ans = self.s.isAnagram(s, t)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
