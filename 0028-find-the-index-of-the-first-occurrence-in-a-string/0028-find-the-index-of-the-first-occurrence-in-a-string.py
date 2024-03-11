class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if needle in haystack:
            
            for i in range(0,len(haystack)):
                if haystack[i]==needle[0]:
                    if haystack[i:i+len(needle)]==needle:
                        return i
                else:
                    i=i+len(needle)
            
            return -1
        else:
            return -1
        