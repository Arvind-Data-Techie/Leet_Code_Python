class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        reversed_string=str(x)[::-1]
        if int(reversed_string)==x:
            return True
        else:
            return False
        