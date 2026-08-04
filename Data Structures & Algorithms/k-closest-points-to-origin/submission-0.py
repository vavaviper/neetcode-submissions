class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []
        for i in points:
            dist = math.sqrt((i[0] - 0)**2 + (i[1] - 0)**2)
            heapq.heappush(heap, (dist, i))
        
        output = []
        for i in range(k):
            output.append(heapq.heappop(heap)[1])
        
        return output

        