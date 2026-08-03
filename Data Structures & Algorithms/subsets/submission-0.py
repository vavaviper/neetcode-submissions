class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        path = []
        
        def dfs(i):
            if i >= len(nums):
                output.append(path.copy())
                return 
            
            #include i
            path.append(nums[i])
            dfs(i+1)
            #include [] instead
            path.pop()
            dfs(i+1)
        dfs(0)
        return output