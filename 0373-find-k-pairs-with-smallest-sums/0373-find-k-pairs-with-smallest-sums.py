class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        que = []
        heapq.heapify(que)
        heapq.heappush(que, (nums1[0]+nums2[0], 0, 0))
        i, j = 0, 0
        ans = []
        check = set()
        while len(ans) < k:
            t = heapq.heappop(que)
            a, b, c = t
            if (b, c) in check:
                continue
            check.add((b, c))
            ans.append((nums1[b], nums2[c]))
            if b+1 < len(nums1):
                heapq.heappush(que, (nums1[b+1]+nums2[c], b+1, c))
            if c+1 < len(nums2):
                heapq.heappush(que, (nums1[b]+nums2[c+1], b, c+1))
        return ans