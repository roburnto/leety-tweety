# Last updated: 1/12/2026, 1:41:42 PM
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        
        #dimensions of forest
        rows, cols = len(forest),len(forest[0])
        
        #extract all the tree and sort by height
        trees = sorted((height,r,c) for r,row in enumerate(forest) for c, height in enumerate(row) if height > 1)
        
        #bfs to calculate shortest path betwen two points
        
        def bfs(start_r, start_c, target_r, target_c):
            visited = set()
            
            q = deque([(start_r, start_c, 0)]) # (row, col, steps)
            
            visited.add((start_r,start_c))
            
            while q:
                
                r,c,steps = q.popleft()
                
                if(r,c) ==(target_r, target_c):
                    return steps
                
                for dr,dc in [(1,0),(-1,0),(0,1), (0,-1)]:
                    nr, nc = r+dr, c+dc
                    
                    if 0 <= nr < rows and  0 <= nc < cols and (nr,nc) not in visited and forest[nr][nc] >0:
                        visited.add((nr,nc))
                        q.append((nr,nc, steps+1))
                        
            return -1
        
        total_steps = 0
        start_r, start_c = 0,0
        
        for height, tree_r, tree_c in trees:
            steps = bfs(start_r, start_c, tree_r, tree_c)
            
            if steps == -1:
                return -1 # tree is unreachable
            
            total_steps += steps
            
            start_r, start_c = tree_r, tree_c
            forest[tree_r][tree_c] = 1
            
        return total_steps