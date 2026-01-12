# Last updated: 1/12/2026, 1:41:26 PM
class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        total = 0
        window_sum = sum(calories[:k])
        
        if window_sum > upper:
            total += 1
        elif window_sum < lower:
            total -=1
            
        for i in range(k, len(calories)):
            window_sum += calories[i] - calories[i - k]
            if window_sum > upper:
                total +=1
            elif window_sum < lower:
                total -=1
                
        return total