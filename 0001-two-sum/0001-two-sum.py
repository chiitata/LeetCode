class Solution:
    def twoSum(self, nums, target):
        targets = {}
        for i in range(len(nums)):
            bar = target - nums[i]
            if nums[i] in targets:
                return [i, targets[nums[i]]]
            targets[bar] = i



        