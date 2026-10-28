class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftArr = self.buildLeftArray(nums)
        rightArr = self.buildRightArray(nums)
        result = []
        for i in range(len(nums)):
            left = 1
            right = 1
            if i > 0:
                left = leftArr[i-1]
            else:
                left = 1
            if i < len(nums) - 1:
                right = rightArr[i+1]
            else:
                right = 1

            result.append(left * right)
        return result

    def buildRightArray(self, nums):
        result = [1] * len(nums)
        result[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            result[i] = nums[i] * result[i+1]
        return result

    def buildLeftArray(self, nums):
        result = [0] * len(nums)
        result[0] = nums[0]
        for i in range(1, len(nums)):
            result[i] = nums[i] * result[i-1]
        return result
        