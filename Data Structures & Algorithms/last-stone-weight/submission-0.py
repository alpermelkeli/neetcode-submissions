import heapq

class Solution:

    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-i for i in stones]
        heapq.heapify(heap)
        
        while len(heap) >= 2:
            first = -1 * heapq.heappop(heap)
            second = -1 * heapq.heappop(heap)
        
            if first == second:
                continue

            if first > second:
                heapq.heappush(heap,-(first-second))

        if len(heap) != 0:
            return -heap[0]
        else:
            return 0