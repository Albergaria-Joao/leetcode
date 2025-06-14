class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairIndex = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if (diff in pairIndex):
                return [i, pairIndex[diff]]
            pairIndex[nums[i]] = i
