class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        if [*map(s.index, s)]==[*map(t.index, t)]:
            return True
        
        return False