class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')':'(','}':'{',']':'['}
        stack=list()
        for i in s:
            if i in mapping.values():
                stack.append(i)
                continue
            if stack and stack[-1]==mapping[i]:
                stack.pop()
                continue
            else:
                return False
        if stack:
            return False
        return True

        