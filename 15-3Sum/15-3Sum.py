# Last updated: 9/3/2025, 4:12:38 PM
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, num in enumerate(nums):
            if num > 0:
                break
            if num == nums[i-1] and i != 0:
                continue

            l, r = i+1, len(nums)-1

            while l < r:
                threesum = num + nums[l] + nums[r]
                if threesum < 0:
                    l += 1
                elif threesum > 0:
                    r -= 1
                else:
                    res.append([num,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
        
        return res