class Solution:
    def countDigits(self, num: int) -> int:
        dup_num=num
        count=0
        while dup_num>0:
            digit=dup_num%10
            if num%digit==0:
                count+=1
            dup_num=dup_num//10
        return count
        