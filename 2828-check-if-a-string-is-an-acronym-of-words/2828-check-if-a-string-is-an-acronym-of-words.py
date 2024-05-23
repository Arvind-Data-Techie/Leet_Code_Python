class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        string=''
        for word in words:
            string=string+word[0]
        if string==s:
            return True
        else:
            return False