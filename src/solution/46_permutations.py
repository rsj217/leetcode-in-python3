import unittest
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums_visit = [False for _ in range(len(nums))]

        def backtrack(nums_visit: List[int], path: List[int]):
            if len(nums) == len(path):
                ans.append(path[:])
                return

            for i, item in enumerate(nums):
                if nums_visit[i]:
                    continue

                nums_visit[i] = True
                path.append(item)
                backtrack(nums_visit, path)
                nums_visit[i] = False
                path.pop()
        backtrack(nums_visit, [])
        return ans



class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([1], [[1]]),
            ([0, 1], [[0,1],[1,0]]),
            ([1, 2, 3], [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]),
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, answer in self.test_case:
            ans = self.s.permute(nums)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
