class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sortednums = sorted(nums)
        hash1 = {}
        for i in sortednums:
            if i in hash1:
                hash1[i] += 1
            else:
                hash1[i] = 1
        return sorted(hash1, key = hash1.get, reverse=True)[:k]