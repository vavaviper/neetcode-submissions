class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        path = []

        def dfs(i, remaining):
            if remaining == 0:
                output.append(path.copy())
                return

            if remaining < 0 or i >= len(nums):
                return

            # take nums[i]
            path.append(nums[i])
            dfs(i, remaining - nums[i])
            path.pop()

            # skip nums[i]
            dfs(i + 1, remaining)
        dfs(0, target)
        return output
