class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        targets = [-x for x in nums]
        ans = []
        target_check = set()
        checked = set()
        for i, target in enumerate(targets):
            if target in target_check:
                continue
            target_check.add(target)
            map = {}
            for j, num in enumerate(nums):
                ber = target - num
                if ber in map:
                    check = tuple(sorted([nums[i], nums[j],nums[map[ber]]]))
                    if  check not in checked:
                        if len({i, j, map[ber]}) == 3:
                            ans.append([nums[i], nums[j], nums[map[ber]]])
                            checked.add(check)
                map[num] = j
        return ans