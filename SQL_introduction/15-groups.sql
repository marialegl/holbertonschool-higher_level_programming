-- Counts the number of records for each score.
-- Sort the results by the number of records in descending order
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;