class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def search(r,c):
            if r < 0 or r >= len(grid):
                return 0
            if c < 0 or c >= len(grid[0]):
                return 0 
            if grid[r][c] == 0:
                return 0
            
            if grid[r][c] == 1:
                print("island at", r, c)
                grid[r][c] = 0

                up = search(r+1,c)
                down = search(r-1,c)
                left = search(r,c+1)
                right = search(r,c-1)
                return 1 + up + down + left + right
        
        output = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                print("searching",r,c)
                output = max(output, search(r,c))
        return output

            