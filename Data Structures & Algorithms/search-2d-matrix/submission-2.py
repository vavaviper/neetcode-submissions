class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for m in matrix:
            if m[-1] >= target:
                for n in m:
                    if n == target:
                        return True

        return False