# Last updated: 1/12/2026, 1:41:28 PM
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        buck1 = []
        
        buck2 = []
        
        count = {}
        
        for num in arr1:
            count[num] = count.get(num,0)+1
        
        for num in arr2:
            if num in count:
                buck1.extend([num]*count[num])
                del count[num]
                
        for num in sorted(count.keys()):
            buck2.extend([num]*count[num])
            
            
        
        
        
        return buck1 + buck2