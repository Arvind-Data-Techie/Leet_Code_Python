from datetime import datetime

class Solution:
    
       
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        
        def get_date(dates):
            year, month, day=map(int, dates.split('-'))
            return date(year,month,day)

        return abs((get_date(date1)-get_date(date2)).days)

    
    
        
    
    