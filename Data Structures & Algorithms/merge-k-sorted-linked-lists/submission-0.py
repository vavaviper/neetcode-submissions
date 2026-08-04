import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        # Put the first node from every list into the heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode()
        curr = dummy

        while heap:
            val, i, node = heapq.heappop(heap)

            # Add this node to our result
            curr.next = node
            curr = curr.next

            # Put the next node from this list into the heap
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next