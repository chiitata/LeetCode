class Solution:
    def isValid(self, s: str) -> bool:
        que = deque()
        for i in s:
            if i == "(" or i == "{" or i == "[":
                que.append(i)
            elif i == ")":
                if len(que) == 0:
                    return False
                bra = que.pop()
                if bra != "(":
                    return False
            elif i == "}":
                if len(que) == 0:
                    return False
                bra = que.pop()
                if bra != "{":
                    return False
            elif i == "]":
                if len(que) == 0:
                    return False
                bra = que.pop()
                if bra != "[":
                    return False
        if len(que) == 0:
            return True
        return False
        