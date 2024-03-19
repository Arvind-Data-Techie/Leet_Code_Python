SELECT w1.id
FROM Weather w1
JOIN Weather w2 ON DATEDIFF(DAY, w2.recordDate, w1.recordDate) = 1
AND w1.Temperature > w2.Temperature