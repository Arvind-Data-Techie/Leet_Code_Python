class Solution:

    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub(r'[^\w\s]', ' ', paragraph.lower())
        self.dictionary = {}
        lst = paragraph.split()
        for word in lst:
            self.count(word)
        for word in banned:
            try:
                del self.dictionary[word]
            except KeyError:
                pass

        max_word = max(zip(self.dictionary.values(), self.dictionary.keys()))[1]
        return max_word

    def count(self,word):
        if word in self.dictionary:
            self.dictionary[word] += 1
        else:
            self.dictionary.update({word: 1})