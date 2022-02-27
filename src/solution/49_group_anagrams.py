"""
`Problem <https://leetcode-cn.com/problems/group-anagrams/>`_
-----------------------------------------------------------------------------
49. 字母异位词分组

给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
字母异位词 是由重新排列源单词的字母得到的一个新单词，所有源单词中的字母通常恰好只用一次。

::

    示例 1:

    输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
    示例 2:

    输入: strs = [""]
    输出: [[""]]
    示例 3:

    输入: strs = ["a"]
    输出: [["a"]]


    提示：

    1 <= strs.length <= 104
    0 <= strs[i].length <= 100
    strs[i]仅包含小写字母



Tips
------

1. 字母异或词的单词排序是同一个，可以作为key
2. key相同的value的是相同的异或词列表

时间：O(mlogm+n)
空间：O(n)

Answer
------

"""
import unittest
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = dict()  # k 字符排序后， v 原始字符列表

        for item in strs:
            arr = list(item)
            arr.sort()
            k = "".join(arr)
            dct.setdefault(k, []).append(item)

        return list(dct.values())


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            (["eat", "tea", "tan", "ate", "nat", "bat"], [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]),
            ([""], [[""]]),
            (["a"], [["a"]]),
        ]
        self.s = Solution()

    def test_solution(self):
        for strs, answer in self.test_case:
            ans = self.s.groupAnagrams(strs)
            self.assertListEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
