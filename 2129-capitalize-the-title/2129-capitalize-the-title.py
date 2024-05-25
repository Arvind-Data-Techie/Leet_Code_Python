class Solution:
    def capitalizeTitle(self, title: str) -> str:
        target=[]
        
        return ' '.join([word.lower() if len(word)<3 else word.capitalize() for word in title.split(' ')])
        