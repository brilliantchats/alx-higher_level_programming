-- Lists the num of records with the same score in second table
SELECT score, COUNT(score) AS number
	FROM second_table
       	GROUP BY score
       	ORDER BY number DESC;
