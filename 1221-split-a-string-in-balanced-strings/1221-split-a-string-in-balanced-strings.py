class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = l = 0
        ans = sum(1 for c in s if (l := l + 1 if c == 'L' else l - 1) == 0)
        return ans