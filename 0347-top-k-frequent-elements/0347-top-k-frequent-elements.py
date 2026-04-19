class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num = {}
        for i in nums:
            if i in num:
                num[i] += 1
            else:
                num[i] = 1
        ans = heapq.nlargest(k, num, key=num.get)
        return ans