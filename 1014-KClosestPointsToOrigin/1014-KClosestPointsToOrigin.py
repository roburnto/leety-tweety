# Last updated: 1/12/2026, 1:41:35 PM
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        sorted_distance = sorted(points, key=lambda point: point[0]**2 + point[1]**2)
        
        return sorted_distance[:k]