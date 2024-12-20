# Write your MySQL query statement below
SELECT curr.id AS Id
FROM Weather curr
JOIN Weather prev 
  ON prev.recordDate = DATE_SUB(curr.recordDate, INTERVAL 1 DAY)
WHERE curr.temperature > prev.temperature;

