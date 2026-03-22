class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for i in range(len(strs)):
            sorted_str = "".join(sorted(strs[i]))
            if sorted_str in map:
                map[sorted_str].append(strs[i])
            else:
                map[sorted_str] = [strs[i]]
        ans = []
        for i, string in enumerate(map):
            ans.append(map[string])
        return ans