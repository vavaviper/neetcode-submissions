class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        grid = [set() for _ in range(9)]
        horizontal = set()
        vertical = [set() for _ in range(9)]

        for x in range(len(board)):
            horizontal = set()
            for y in range(len(board)):
                curr = board[x][y]
                if curr != '.':
                    if curr in horizontal:
                        return False
                    else:
                        horizontal.add(curr)
                    
                    if curr in vertical[y]:
                        return False
                    else:
                        vertical[y].add(curr)
                    box = (x//3) * 3 + (y//3) 
                    if curr in grid[box]:
                        return False
                    else:
                        grid[box].add(curr)   
        return True    