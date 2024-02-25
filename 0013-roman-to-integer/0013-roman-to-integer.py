class Solution:
    
    def romanToInt(self, s: str) -> int:
        
        val=0
        
        if 'IV' in s:
            val += 4
            s = s.replace('IV', '')

        if 'IX' in s:
            val += 9
            s = s.replace('IX', '')

        if 'XL' in s:
            val += 40
            s = s.replace('XL', '')

        if 'XC' in s:
            val += 90
            s = s.replace('XC', '')

        if 'CD' in s:
            val += 400
            s = s.replace('CD', '')

        if 'CM' in s:
            val += 900
            s = s.replace('CM', '')

        
        for i in s:
            if i == 'I':
                val += 1
            elif i == 'V':
                val += 5
            elif i == 'X':
                val += 10
            elif i == 'L':
                val += 50
            elif i == 'C':
                val += 100
            elif i == 'D':
                val += 500
            elif i == 'M':
                val += 1000
                
        return val
            
        