class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        m = self.buildMap(numbers, target)
        for i in range(len(numbers)):
            if numbers[i] in m.keys():
                return [i + 1 , m[numbers[i]] + 1]


    
    
    
    def buildMap(self, numbers, target):
        m = {}

        for i in range(len(numbers)):
            m[target - numbers[i]] = i
        return m