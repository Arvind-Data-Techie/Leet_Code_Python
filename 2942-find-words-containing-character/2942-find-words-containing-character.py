class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
      
        return [e for e, word in enumerate(words) if x in word]