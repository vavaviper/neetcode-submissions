class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0

        def search(r,c):
            if r < 0 or r >= len(grid):
                return False
            if c < 0 or c >= len(grid[0]):
                return False
            if grid[r][c] == "0":
                return False
            
            if grid[r][c] == "1":
                
                grid[r][c] = "0"
                search(r+1 , c)
                search(r-1 , c)
                search(r , c+1)
                search(r , c-1)
                return True
                

        for r in range(len(grid)+1):
            for c in range(len(grid[0])):
                print("im at", r, c)
                if search(r,c):
                    print("island found! at", r, c)
                    islands += 1
        return islands
