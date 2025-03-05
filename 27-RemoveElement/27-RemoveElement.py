class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #count of occurrences
        count = 0
        list_len = len(nums)

        for num in nums:
            if num == val:
                count+=1
        
        for i in range(count):
            nums.remove(val)

        return  list_len-count