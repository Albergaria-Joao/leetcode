class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        pairIndex = {}

        for i, num in enumerate(nums):
            if (num in pairIndex):
                return True
            else:
                pairIndex[num] = i
        return False
