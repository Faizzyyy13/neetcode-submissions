class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset=set()
        length=0
        l,r=0,0
        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l+=1
            charset.add(s[r])
            length=max(length,r-l+1)
        return length