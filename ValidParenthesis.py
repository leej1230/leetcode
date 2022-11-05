class Solution:
    def isValid(self, s: str) -> bool:
        par = {
            '(':')',
            '{':'}',
            '[':']'
        }
        stack = []
        op = ['(','{','[']
        cl = [')','}',']']
        for p in s:
            if p in op:
                stack.append(par[p])
            if p in cl:
                if len(stack) == 0:
                    return False
                if p != stack[-1]:
                    return False
                stack.pop()
        if len(stack) != 0:
            return False
        return True