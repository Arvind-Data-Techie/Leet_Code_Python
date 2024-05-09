class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [''] * len(s)
        for index, alph in enumerate(s):
            res[indices[index]] = alph
        return "".join (res)