# Write your MySQL query statement below

select m.name as Employee
from Employee as e
inner join Employee as m
on m.ManagerId=e.id
where m.salary>e.salary
