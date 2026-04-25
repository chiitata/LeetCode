class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [(nums[0], nums[0], nums[0])]
        for i in range(1, len(nums)):
            ans, min_num, sum_num = dp[-1]
            sum_num = sum_num + nums[i]
            ans = max(sum_num-min_num, ans)
            ans = max(sum_num-0, ans)
            min_num = min(min_num, sum_num)
            dp.append((ans, min_num, sum_num))
        return max(dp)[0]
