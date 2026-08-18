class Solution:
    def findMin(self, nums: List[int]) -> int:
        import math
        lowestnum = math.inf

        for i in nums:
            if i < lowestnum:
                lowestnum = i
        return lowestnum