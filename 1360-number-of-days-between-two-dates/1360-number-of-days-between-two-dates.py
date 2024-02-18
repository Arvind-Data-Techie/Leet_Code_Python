from datetime import datetime

class Solution:
    
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        year, month, day = map(int, date1.split('-'))
        date_1=date(year,month,day)
        year, month, day = map(int, date2.split('-'))
        date_2 = date(year, month, day)
        return abs((date_1-date_2).days)
        
    
    