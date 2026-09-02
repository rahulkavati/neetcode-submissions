class Solution:
    def isPalindrome(self, s: str) -> bool:
        ts = ''
        for c in s:
            if c.isalnum():
                ts+=c.lower()
        return ts == ts[::-1]