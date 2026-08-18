class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        lowestnum = 10000

        for i in nums:
            if i < lowestnum:
                lowestnum = i
        return lowestnum