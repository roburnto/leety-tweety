# Last updated: 1/12/2026, 1:41:46 PM
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = defaultdict(int)
        
        for c in s:
            count[c] += 1
            
        for i, c in enumerate(s):
            if count[c] == 1:
                return i
            
        return -1