class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')':'(','}':'{',']':'['}
        stack=list()
        for i in s:
            if i in mapping.values():
                stack.append(i)
            elif stack and stack[-1]==mapping[i]:
                stack.pop()
            else:
                return False
        if stack:
            return False
        return True

        