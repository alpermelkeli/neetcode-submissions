class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = self.buildMap(nums)
        sortedKeys = [x for x, v in sorted(countMap.items(), key=lambda item: item[1], reverse=True)]
        return sortedKeys[:k]

        


    def buildMap(self, nums: List[int]) -> dict:
        countMap = dict()
        for num in nums: 
            if num in countMap:
                countMap[num] += 1
            else:
                countMap[num] = 1
        return countMap
