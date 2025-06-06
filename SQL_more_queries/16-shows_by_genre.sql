-- Write a script that lists alll shows, and all genres linked to that show, from the database --
SELECT s.title, g.name
FROM tv_shows s
LEFT JOIN tv_show_genres sg ON s.id = sg.show_id
LEFT JOIN tv_genres g ON sg.genre_id = g.id
ORDER BY s.title ASC, g.name ASC;
