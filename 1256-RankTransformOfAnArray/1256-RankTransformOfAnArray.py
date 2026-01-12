# Last updated: 1/12/2026, 1:41:27 PM
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr:
            return []
        
        unique = sorted(set(arr))
        
        rank_map = {val: rank+1 for rank, val in enumerate(unique)}
        
        return [rank_map[num] for num in arr]