class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        
        ascii_value_list=[ord(i) for i in letters]
        
        
        
        for i in ascii_value_list:
            if i>ord(target):
                return chr(i)
                
        
        return chr(ascii_value_list[0])
        