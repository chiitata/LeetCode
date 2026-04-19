class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num = defaultdict(int)
        for i in nums:
            num[i] += 1
        ans = heapq.nlargest(k, num, key=num.get)
        return ans