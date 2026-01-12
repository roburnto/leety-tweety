# Last updated: 1/12/2026, 1:41:40 PM
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        original_color = image[sr][sc]
        
        #if starting pixel is already the target color, return the image
        if original_color == color:
            return image
        
        #helper function
        def dfs(r,c):
            #check boundaries and if the pixel matches the original color
            if r < 0 or r>=rows or c<0 or c>= cols or image[r][c]!= original_color:
                return
            
            #update image color
            image[r][c] = color
            
            #recursive calls for all four directions
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        #start DFS from the given starting pixel
        dfs(sr,sc)
        
        return image