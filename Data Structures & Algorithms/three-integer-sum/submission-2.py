class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        nums.sort()
        output = []
        seen = set()

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                third = -(nums[i] + nums[j])

                if third not in freq:
                    continue

                need = {}

                for x in (nums[i], nums[j], third):
                    if x in need:
                        need[x] += 1
                    else:
                        need[x] = 1

                valid = True
                for x in need:
                    if freq[x] < need[x]:
                        valid = False
                        break

                if valid:
                    triplet = tuple(sorted([nums[i], nums[j], third]))
                    if triplet not in seen:
                        seen.add(triplet)
                        output.append(list(triplet))

        return output