class Solution:
    def twoSum(self, nums, target):
        num_map = {}
        for i, num in enumerate(nums):
            ber = target - num
            if ber in num_map:
                return [num_map[ber], i]
            num_map[num] = i                    



        