class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        output = []

        for interval in intervals:
            # If output is empty, add the first interval
            if not output:
                output.append(interval)

            # If current interval overlaps with the last merged interval
            elif interval[0] <= output[-1][1]:
                # Extend the ending point
                output[-1][1] = max(output[-1][1], interval[1])

            # No overlap
            else:
                output.append(interval)

        return output