class Solution:
    def isPalindrome(self, s: str) -> bool:
        pal_word=re.sub(r'[^a-zA-Z0-9]','', s.lower())
        if pal_word==pal_word[::-1]:
            return True
        else:
            return False
        