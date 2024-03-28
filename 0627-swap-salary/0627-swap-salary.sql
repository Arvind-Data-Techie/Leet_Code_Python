UPDATE salary
SET sex = CASE WHEN Sex='m' THEN 'f' ELSE 'm'
END;