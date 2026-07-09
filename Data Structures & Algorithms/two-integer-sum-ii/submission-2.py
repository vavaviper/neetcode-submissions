class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            comp = numbers[left] + numbers[right]
            if comp == target:
                return [left + 1, right + 1]
            elif comp > target:
                right -= 1
            elif comp < target:
                left += 1