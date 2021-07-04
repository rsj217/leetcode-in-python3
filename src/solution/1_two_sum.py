"""
`Problem <https://leetcode-cn.com/problems/two-sum/>`_
--------------------------------------------------------

定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。

::

    示例 1：

    入：nums = [2,7,11,15], target = 9
    出：[0,1]
    释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

    示例 2：

    入：nums = [3,2,4], target = 6
    出：[1,2]

    示例 3：

    入：nums = [3,3], target = 6
    出：[0,1]


    提示：

    2 <= nums.length <= 103
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    只会存在一个有效答案

Tips
------

.. image:: ../../img/Spanish.jpg



Answer
------

"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        t = dict()
        for i in range(len(nums)):
            index = t.get(target - nums[i])
            if index is not None:
                return [index, i]
            t[nums[i]] = i
        return []
