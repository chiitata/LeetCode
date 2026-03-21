class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        max_len = float("inf")
        for i in range(len(strs)):
            max_len = min(max_len, len(strs[i]))
        ans = []
        if max_len == 0:
            return ""
        for i in range(max_len):
            for j in range(len(strs)):
                if j == 0:
                    tmp = strs[0][i]
                    continue
                if tmp != strs[j][i]:
                    return "".join(ans)
            else:
                ans.append(tmp)
        else:
            return "".join(ans)
