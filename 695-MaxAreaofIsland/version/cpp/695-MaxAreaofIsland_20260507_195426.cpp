// Last updated: 5/7/2026, 7:54:26 PM
1class Solution {
2   public:
3    int maxAreaOfIsland(vector<vector<int>>& grid) {
4        int ROWS = grid.size();
5        int COLS = grid[0].size();
6        int maxArea = 0;
7        for (int r = 0; r < ROWS; r++) {
8            for (int c = 0; c < COLS; c++) {
9                if (grid[r][c] == 1) {
10                    maxArea = max(maxArea, dfs(grid, r, c));
11                }
12            }
13        }
14        return maxArea;
15    }
16
17   private:
18    int dfs(vector<vector<int>>& grid, int r, int c) {
19        int ROWS = grid.size();
20        int COLS = grid[0].size();
21        if (r < 0 || c < 0 || r >= ROWS || c >= COLS || grid[r][c] == 0) {
22            return 0;
23        }
24        grid[r][c] = 0;
25        return 1 + dfs(grid, r + 1, c) + dfs(grid, r - 1, c) + dfs(grid, r, c + 1) +
26               dfs(grid, r, c - 1);
27    }
28};
29