SELECT MAX(num) as num FROM
(SELECT num from MyNumbers
GROUP BY num
HAVING COUNT(num)=1
) a


