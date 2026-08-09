class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        seenlist = []

        for num in nums:
            if num in seenlist:
                return True
            else:
                seenlist.append(num)
        return False