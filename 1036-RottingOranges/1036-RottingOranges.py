# Last updated: 1/12/2026, 1:41:34 PM
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        
        q = deque()
        
        fresh = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))  # Add rotten orange to the queue
                elif grid[r][c] == 1:
                    fresh += 1
                
        if fresh == 0:
            return 0
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        minutes = 0
        
        while q:
            minutes +=1
            for _ in range(len(q)):
                x,y = q.popleft()
                
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        q.append((nx, ny))
                        fresh -= 1
                        
        return minutes - 1 if fresh == 0 else -1