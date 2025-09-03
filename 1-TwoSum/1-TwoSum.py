# Last updated: 9/3/2025, 3:25:51 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}

        for i, num  in enumerate(nums):
            complement = target-num
            if complement in num_map:
                return [i,num_map[complement]]
            num_map[num] = i