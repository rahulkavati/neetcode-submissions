class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numSets = set(nums)
        return len(numSets) != len(nums)