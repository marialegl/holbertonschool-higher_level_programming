-- List all records with a score >= 10 in the second table.
-- Shows both score and name.
-- Records are sorted by score.
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;