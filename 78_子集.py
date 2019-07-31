'''
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
说明：解集不能包含重复的子集。
示例:
输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''


class Solution:
    def subsets(self, nums):
        res = []
        n = len(nums)

        # def __backtrace(combination: list, digits: list):
        #     # if len(digits) == 0:
        #     #     return
        #     res.append(combination)
        #     for i in digits:
        #         temp = [digit for digit in digits if digit != i]
        #         __backtrace(combination+[i], temp)

        def __backtrace(combination, i):
            res.append(combination)
            for j in range(i, n):
                __backtrace(combination + [nums[j]], j + 1)

        if nums:
            __backtrace([], 0)
        return res


s = Solution()
nums = [1, 2, 3]
print(s.subsets(nums))
