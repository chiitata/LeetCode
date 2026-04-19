class Solution:
    def firstUniqChar(self, s: str) -> int:
        a = Counter(s)
        for i in range(len(s)):
            if a[s[i]] == 1:
                return i
        else:
            return -1