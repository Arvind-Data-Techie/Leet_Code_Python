class Solution:
    def capitalizeTitle(self, title: str) -> str:
        target=[]
        for word in title.split(' '):
            if len(word)<3:
                target.append(word.lower())
            else:
                target.append(word.capitalize())
                
        print(' '.join(target))
        return ' '.join(target)