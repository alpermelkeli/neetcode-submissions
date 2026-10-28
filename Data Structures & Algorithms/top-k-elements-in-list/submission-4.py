import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = self.buildMap(nums)
        heap = []

        for (num, freq) in countMap.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)

        return [num for freq, num in heap]
        


    def buildMap(self, nums: List[int]) -> dict:
        countMap = dict()
        for num in nums: 
            if num in countMap:
                countMap[num] += 1
            else:
                countMap[num] = 1
        return countMap
