-- Will show all shows and their genres, with NULL in case a show has no genre
SELECT title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_shows_genres ON tv_shows.id = tv_shows_genres.show_id
LEFT JOIN tv_genres ON tv_genres.id = tv_show_genres.genere_id
ORDER BY title ASC, tv_genres.name ASC;