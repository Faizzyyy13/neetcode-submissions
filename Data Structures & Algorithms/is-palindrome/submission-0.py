class Solution:
    def isPalindrome(self, s: str) -> bool:
        filt="".join(c.lower()for c in s if c.isalnum())
        return filt==filt[::-1]