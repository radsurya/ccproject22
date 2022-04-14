DROP DATABASE IF EXISTS mubi_data;
CREATE DATABASE IF NOT EXISTS mubi_data;
USE mubi_data;

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

