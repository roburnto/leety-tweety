# Last updated: 1/12/2026, 1:41:50 PM
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        
        for i in range(len(nums)):
            res += i - nums[i]
            
        return res
        
        