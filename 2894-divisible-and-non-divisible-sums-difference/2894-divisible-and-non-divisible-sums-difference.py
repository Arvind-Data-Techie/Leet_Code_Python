class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        divisible_list=[]
        non_divisible_list=[]
        for i in range(1,n+1):
            if i%m==0:
                divisible_list.append(i)
            else:
                non_divisible_list.append(i)
        return sum(non_divisible_list)-sum(divisible_list)
        