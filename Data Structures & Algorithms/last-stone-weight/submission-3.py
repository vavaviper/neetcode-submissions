import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        # create max heap using negative numbers
        for i in stones:
            heapq.heappush(heap, -i)

        while len(heap) >= 2:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)

            if x > y:
                heapq.heappush(heap, -(x - y))

        if len(heap) == 1:
            return -heap[0]

        return 0