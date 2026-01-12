# Last updated: 1/12/2026, 1:41:36 PM
class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        seen_states = {}
        steps = 0
        
        while n > 0:
            next_day = [0] * len(cells)
            
            for i in range(1,len(cells)-1):
                next_day[i]  = 1 if cells[i-1] == cells[i+1] else 0
            
            state_tuple = tuple(next_day)
            
            if state_tuple in seen_states:
                
                cycle_length = steps- seen_states[state_tuple]
                n %= cycle_length
                if n == 0:
                    break
            else:
                seen_states[state_tuple] = steps
            
            cells = next_day
            steps +=1
            
            n-=1
        
        return cells