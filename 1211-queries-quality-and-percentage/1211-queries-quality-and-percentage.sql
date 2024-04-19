SELECT query_name,
round(SUM(rating/position)/COUNT(rating/position),2) as 'quality',
round(AVG(CASE WHEN rating < 3 THEN 1 ELSE 0 END)*100.0,2) as 'poor_query_percentage'
FROM Queries 
group by query_name
HAVING query_name is not null

