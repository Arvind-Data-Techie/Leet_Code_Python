class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        unshuffled_chars = [''] * len(s)
        for i, idx in enumerate(indices):
            unshuffled_chars[idx] = s[i]
        unshuffled_string = ''.join(unshuffled_chars)
        return unshuffled_string
            