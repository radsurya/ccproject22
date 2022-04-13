-- Subject: Cloud Computing 2021/2022 | Project - Part 3
-- Authors: Group 3
---- Radica Giva (no. 44311)
---- Filipe Pedroso (no. 51958)
---- Jonathan Gehmayr (no. 57267)
-- Description: This file contains all queries to create tables in SQL for the project
-- Tables list: 1 - Movie, 2 - Rating


-- 1 - Create "Movie" table
DROP TABLE IF EXISTS movie;
CREATE TABLE movie (
	movie_id VARCHAR(255) PRIMARY KEY, 
	movie_title VARCHAR(255), 
	movie_release_year FLOAT, 
	movie_url VARCHAR(255), 
	movie_title_language VARCHAR(255), 
	movie_popularity INT, 
	movie_image_url VARCHAR(255), 
	director_id VARCHAR(255), 
	director_name VARCHAR(255),
	director_url VARCHAR(255),
	average_rating FLOAT
);


-- 2 - Create "Rating" table
DROP TABLE IF EXISTS rating;
CREATE TABLE rating (
	movie_id VARCHAR(255), 
	rating_id VARCHAR(255) PRIMARY KEY, 
	rating_url VARCHAR(255), 
	rating_score FLOAT,
	rating_timestamp_utc TIMESTAMP, 
	critic TEXT, 
	critic_likes INT, 
	critic_comments INT, 
	user_id VARCHAR(255), 
	user_trialist BOOLEAN, 
	user_subscriber BOOLEAN,
	user_eligible_for_trial BOOLEAN, 
	user_has_payment_method BOOLEAN,
	FOREIGN KEY (movie_id) REFERENCES movie(movie_id)
);

