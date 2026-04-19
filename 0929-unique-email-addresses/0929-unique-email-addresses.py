class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        domain, address = set(), set()
        ans = 0
        for i in range(len(emails)):
            email = emails[i]
            a, b = email.split("@")[0].split("+")[0].replace(".", ""), email.split("@")[1]
            if a not in address or b not in domain:
                ans += 1
                domain.add(b)
                address.add(a)
        return ans