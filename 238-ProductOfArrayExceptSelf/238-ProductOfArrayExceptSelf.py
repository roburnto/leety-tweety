# Last updated: 1/12/2026, 1:41:53 PM
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [1] * n

        # prefix pass: res[i] holds product of elements before i
        pref = 1
        for i in range(n):
            res[i] = pref
            pref *= nums[i]

        # postfix pass: multiply by product of elements after i
        post = 1
        for i in range(n - 1, -1, -1):
            res[i] *= post
            post *= nums[i]

        return res