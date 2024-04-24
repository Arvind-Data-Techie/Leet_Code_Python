class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stone_count=0
        for s in jewels:
            stone_count+=stones.count(s)
        return stone_count
            
        