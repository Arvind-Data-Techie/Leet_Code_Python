/* Write your T-SQL query statement below */

SELECT name,bonus
FROM Employee e
LEFT JOIN Bonus b ON e.empId=b.empId 
where bonus is null or bonus<1000