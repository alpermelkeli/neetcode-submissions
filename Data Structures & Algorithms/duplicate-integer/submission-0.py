class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numCounts = dict()
        for i in nums:
            if i not in numCounts:
                numCounts[i] = 1
            else:
                return True
        return False

        