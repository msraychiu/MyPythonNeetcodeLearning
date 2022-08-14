class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2: return False
        stack = []
        set = ["{", "(", "["]
        map = {"}": "{", ")": "(", "]": "["}

        for c in s:
            if c in set:
                stack.append(c)
            elif len(stack) == 0 or map.get(c) != stack.pop():
                return False

        return len(stack) == 0
