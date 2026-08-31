class Solution:
    def isValid(self, s: str) -> bool:
        key = {')':'(', ']':'[', '}': '{'}
        stack = []

        for char in s:
            if char not in key:
                stack.append(char)
            else: 
                if not stack:
                    return False
                else: 
                    if stack[-1]==key[char]:
                        stack.pop()
                    else:
                        return False
        return len(stack)==0