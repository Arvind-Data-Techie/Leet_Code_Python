SELECT a.Id AS Id
FROM Weather a
JOIN Weather b
ON a.RecordDate = DATEADD(DAY, 1, b.RecordDate)
WHERE a.Temperature > b.Temperature