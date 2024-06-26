-- Lists all genres in hbtn_0d_tvshows.
-- shows the number of programs linked to each one.
-- Don't show a genre that doesn't have any programs linked to it.
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_show_genres
JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;