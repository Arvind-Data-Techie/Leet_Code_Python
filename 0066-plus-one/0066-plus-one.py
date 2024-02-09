class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_integer=[str(i) for i in digits]
        added_integer=int("".join(str_integer))+1
        return [int(x) for x in str(added_integer)]
        