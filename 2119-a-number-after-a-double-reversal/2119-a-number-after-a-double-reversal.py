class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        reverse_string=str(num)[::-1]
        reverse_string = re.sub('^0+(?!$)', "", reverse_string) 
        print(reverse_string)
        if str(num)==reverse_string[::-1]:
            return True
        else:
            return False
        